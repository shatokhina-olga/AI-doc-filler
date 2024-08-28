import os
from flask import Flask, render_template, request, send_file, Response
from templates_config import get_template_details  # Импорт настроек шаблонов
from pdf_handling import create_text_overlay, add_text_to_pdf
from functools import wraps
import logging
import traceback

app = Flask(__name__)
app.config['DEBUG'] = True  # Включаем режим отладки

# Настройка логирования
logging.basicConfig(filename='app.log', level=logging.DEBUG)


# Определение базового пути для шаблонов PDF
if os.environ.get('PYTHONANYWHERE_DOMAIN'):
    # Мы на PythonAnywhere
    BASE_PATH = '/home/AntonSh/mysite'
else:
    # Мы в локальной среде
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))


# Функция для получения правильного пути к шаблону
def get_template_path(template_name):
    return os.path.join(BASE_PATH, 'static', 'formTemplates', f"{template_name}.pdf")


# Словарь пользователей и паролей
users = {
    "Anton": "Anton123",
    "Olya": "Olya123",
    "Sasha": "Sasha2507",
    "Arthur": "Arthur2507",
    "Aleksandra": "A0208",
    "Vitalii": "V2008",
}


def check_auth(username, password):
    return username in users and users[username] == password


def authenticate():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


@app.route('/', methods=['GET', 'POST'])
@requires_auth
def index():
    return render_template('index.html')


@app.route('/generate', methods=['GET', 'POST'])
@requires_auth
def generate_document():
    if request.method == 'POST':
        try:
            logging.debug("Начало генерации документа")
            # Получаем название выбранного шаблона из формы
            chosen_template = request.form['template']
            logging.debug(f"Выбранный шаблон: {chosen_template}")
            # Получаем детали шаблона из конфигурационного файла
            template_details = get_template_details(chosen_template)
            logging.debug(f"Получены детали шаблона")

            text_items = []
            # Проходим по всем текстовым элементам, определенным в шаблоне
            for item in template_details.get('text_items', []):
                if 'keys' in item:
                    # Собираем значения полей формы для данного элемента, удаляя пробелы по краям
                    values = [request.form.get(key, '').strip() for key in item['keys']]
                    logging.debug(f"Значения для {item['keys']}: {values}")
                    # Специальная обработка для поля адреса, чтобы избежать лишних запятых
                    if item['format'] == '{}, {}, {}' and (
                            (item['keys'] == ['adressStreet', 'adressBuilding', 'adressFlat']) or
                            (item['keys'] == ['adressStreetSpouse', 'adressBuildingSpouse', 'adressFlatSpouse'])):
                        # Удаляем пустые значения, чтобы не добавлять лишние запятые
                        values = [v for v in values if v]
                        formatted_text = ', '.join(values)
                    else:
                        # Используем заданный формат для объединения значений
                        formatted_text = item['format'].format(*values)
                    # Создаем элемент текста для PDF
                    text_item = {
                        'text': formatted_text,
                        'x': item['x'],
                        'y': item['y'],
                        'font': item['font'],
                        'font_size': item['font_size']
                    }
                else:
                    # Обработка простых текстовых полей, не требующих специального форматирования
                    form_value = request.form.get(item['text'], 'Default Value')
                    text_item = {
                        'text': form_value,
                        'x': item['x'],
                        'y': item['y'],
                        'font': item['font'],
                        'font_size': item['font_size']
                    }
                text_items.append(text_item)

            logging.debug(f"Сформировано {len(text_items)} текстовых элементов")

            # Обработка выбора из выпадающих списков для размещения крестиков
            selectors = template_details.get('selectors', {})
            for selector_name, options in selectors.items():
                selected_option = request.form.get(selector_name)
                if selected_option and selected_option in options:
                    coordinates = options[selected_option]
                    # Добавление крестика в выбранное место
                    text_items.append({
                        'text': 'X',  # Символ для отображения
                        'x': coordinates['x'],
                        'y': coordinates['y'],
                        'font': 'Helvetica',  # Можно изменить на нужный шрифт
                        'font_size': 10  # Или другой размер, который требуется
                    })

            # Используем функцию для получения пути к шаблону
            input_pdf_path = get_template_path(chosen_template)
            logging.debug(f"Путь к шаблону PDF: {input_pdf_path}")

            # Проверяем существование файла
            if not os.path.exists(input_pdf_path):
                logging.error(f"Файл не найден: {input_pdf_path}")
                return "Шаблон PDF не найден. Пожалуйста, проверьте наличие файла на сервере.", 404

            # Создаем PDF с текстовыми элементами
            pdf_output = add_text_to_pdf(input_pdf_path, text_items)
            logging.debug("PDF успешно создан")
            # Формируем имя файла для сохранения
            output_filename = request.form['fullName'] + '_' + chosen_template + '.pdf'
            # Отправляем файл пользователю
            logging.debug(f"Отправка файла пользователю: {output_filename}")
            return send_file(pdf_output, as_attachment=True, download_name=output_filename)

        except Exception as e:
            logging.error(f"Произошла ошибка при генерации документа: {str(e)}")
            logging.error(traceback.format_exc())
            return "Произошла ошибка при генерации документа. Пожалуйста, проверьте логи сервера.", 500

    # Отображаем форму для генерации документов
    return render_template('form_generation_page.html')


if __name__ == '__main__':
    app.run(debug=True)
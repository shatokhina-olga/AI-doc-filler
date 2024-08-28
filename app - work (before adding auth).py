from flask import Flask, render_template, request, send_file
from templates_config import get_template_details # Импорт настроек шаблонов
from pdf_handling import create_text_overlay, add_text_to_pdf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])

def generate_document():
    if request.method == 'POST':
        # Получаем название выбранного шаблона из формы
        chosen_template = request.form['template']
        # Получаем детали шаблона из конфигурационного файла
        template_details = get_template_details(chosen_template)

        text_items = []
        # Проходим по всем текстовым элементам, определенным в шаблоне
        for item in template_details.get('text_items', []):
            if 'keys' in item:
                # Собираем значения полей формы для данного элемента, удаляя пробелы по краям
                values = [request.form.get(key, '').strip() for key in item['keys']]
                # Специальная обработка для поля адреса, чтобы избежать лишних запятых
                if item['format'] == '{}, {}, {}' and ((item['keys'] == ['adressStreet', 'adressBuilding', 'adressFlat']) or
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

        # Формируем путь к файлу шаблона PDF
        # На сервере поменяй путь на /home/AntonSh/mysite/static/
        input_pdf_path = 'static/formTemplates/' + chosen_template + '.pdf'
        # Создаем PDF с текстовыми элементами
        pdf_output = add_text_to_pdf(input_pdf_path, text_items)
        # Формируем имя файла для сохранения
        output_filename = request.form['fullName'] + '_' + chosen_template + '.pdf'
        # Отправляем файл пользователю
        return send_file(pdf_output, as_attachment=True, download_name=output_filename)

    # Отображаем форму для генерации документов
    return render_template('form_generation_page.html')

if __name__ == '__main__':
    app.run(debug=True)

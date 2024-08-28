# templates_config.py



# Словарь для хранения шаблонов и координат текста и крестиков для каждого шаблона
templates_details = {
    'Declaration of no criminal record': {

        'text_items': [
            {
                'keys': ['fullName', 'fullSurname'],
                'format': '{} {}',  # Формат с пробелом между именем и фамилией
                'x': 128, 'y': 691, 'font': 'Helvetica', 'font_size': 12
            },
            {
                'keys': ['adressStreet', 'adressBuilding', 'adressFlat'],
                'format': '{}, {}, {}',
                'x': 210, 'y': 619, 'font': 'Helvetica', 'font_size': 12
            },
            {
                'keys': ['citySpain', 'provinciaSpain'],
                'format': '{}, {}',  # Формат с добавлением слова 'provincia'
                'x': 173, 'y': 595, 'font': 'Helvetica', 'font_size': 12
            },
            {'text': 'Nacinalidad', 'x': 143, 'y': 666, 'font': 'Helvetica', 'font_size': 12},
            {'text': 'passport', 'x': 177, 'y': 642, 'font': 'Helvetica', 'font_size': 12},
            {'text': 'applyCity', 'x': 230, 'y': 363, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyDay', 'x': 329, 'y': 363, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyMonth', 'x': 374, 'y': 363, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyYear', 'x': 471, 'y': 363, 'font': 'Helvetica', 'font_size': 10}



            ],
        },
    'Declaration of no criminal record Spouse': {

        'text_items': [
            {
                'keys': ['fullNameSpouse', 'fullSurnameSpouse'],
                'format': '{} {}',  # Формат с пробелом между именем и фамилией
                'x': 128, 'y': 691, 'font': 'Helvetica', 'font_size': 12
            },
            {
                'keys': ['adressStreetSpouse', 'adressBuildingSpouse', 'adressFlatSpouse'],
                'format': '{}, {}, {}',
                'x': 210, 'y': 619, 'font': 'Helvetica', 'font_size': 12
            },
            {
                'keys': ['citySpainSpouse', 'provinciaSpainSpouse'],
                'format': '{}, {}',  # Формат с добавлением слова 'provincia'
                'x': 173, 'y': 595, 'font': 'Helvetica', 'font_size': 12
            },
            {'text': 'NacinalidadSpouse', 'x': 143, 'y': 666, 'font': 'Helvetica', 'font_size': 12},
            {'text': 'passportSpouse', 'x': 177, 'y': 642, 'font': 'Helvetica', 'font_size': 12},
            {'text': 'applyCitySpouse', 'x': 230, 'y': 363, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyDaySpouse', 'x': 329, 'y': 363, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyMonthSpouse', 'x': 374, 'y': 363, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyYearSpouse', 'x': 471, 'y': 363, 'font': 'Helvetica', 'font_size': 10}



            ],
        },
    'Declaration of no criminal record Child': {

        'text_items': [
            {
                'keys': ['fullNameChild', 'fullSurnameChild'],
                'format': '{} {}',  # Формат с пробелом между именем и фамилией
                'x': 128, 'y': 691, 'font': 'Helvetica', 'font_size': 12
            },
            {
                'keys': ['adressStreetChild', 'adressBuildingChild', 'adressFlatChild'],
                'format': '{}, {}, {}',
                'x': 210, 'y': 619, 'font': 'Helvetica', 'font_size': 12
            },
            {
                'keys': ['citySpainChild', 'provinciaSpainChild'],
                'format': '{}, {}',  # Формат с добавлением слова 'provincia'
                'x': 173, 'y': 595, 'font': 'Helvetica', 'font_size': 12
            },
            {'text': 'NacinalidadChild', 'x': 143, 'y': 666, 'font': 'Helvetica', 'font_size': 12},
            {'text': 'passportChild', 'x': 177, 'y': 642, 'font': 'Helvetica', 'font_size': 12},
            {'text': 'applyCityChild', 'x': 230, 'y': 363, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyDayChild', 'x': 329, 'y': 363, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyMonthChild', 'x': 374, 'y': 363, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyYearChild', 'x': 471, 'y': 363, 'font': 'Helvetica', 'font_size': 10}

        ],
    },

    'MI-T': {
        'text_items': [
            # паспорт
            {'text': 'passport', 'x': 112, 'y': 512, 'font': 'Helvetica', 'font_size': 10},
            # NIE
            {'text': 'NIE1', 'x': 345, 'y': 512, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'NIE2', 'x': 375, 'y': 512, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'NIE3', 'x': 525, 'y': 512, 'font': 'Helvetica', 'font_size': 10},
            # имя и фамилия
            {'text': 'fullSurname', 'x': 96, 'y': 499, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'fullName', 'x': 400, 'y': 499, 'font': 'Helvetica', 'font_size': 10},
            # lugar de nacimiento
            {'text': 'cityOriginal', 'x': 129, 'y': 484, 'font': 'Helvetica', 'font_size': 10},
            #дата
            {'text': 'birthDay', 'x': 139, 'y': 471, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthMonth', 'x': 166, 'y': 471, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthYear', 'x': 199, 'y': 471, 'font': 'Helvetica', 'font_size': 10},
            #страна и национальность
            {'text': 'birthCountry', 'x': 257, 'y': 471, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'Nacinalidad', 'x': 449, 'y': 471, 'font': 'Helvetica', 'font_size': 10},
            #имя папы и мамы
            {'text': 'namePapa', 'x': 129, 'y': 458, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'nameMama', 'x': 388, 'y': 458, 'font': 'Helvetica', 'font_size': 10},
            #адрес - улица
            {'text': 'adressStreet', 'x': 129, 'y': 444, 'font': 'Helvetica', 'font_size': 10},
            #адрес - дом и квартира
            {'text': 'adressBuilding', 'x': 491, 'y': 444, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressFlat', 'x': 530, 'y': 444, 'font': 'Helvetica', 'font_size': 10},
            #Licalidad
            {'text': 'citySpain', 'x': 97, 'y': 431, 'font': 'Helvetica', 'font_size': 10},
            #CP и провинция
            {'text': 'indexSpain', 'x': 327, 'y': 431, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'provinciaSpain', 'x': 427, 'y': 431, 'font': 'Helvetica', 'font_size': 10},
            #телефон и емейл
            {'text': 'telephonSpain', 'x': 131, 'y': 407, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'email', 'x': 333, 'y': 407, 'font': 'Helvetica', 'font_size': 10},
            #numero de referancial completo
            {'text': 'numRefComp', 'x': 424, 'y': 212, 'font': 'Helvetica', 'font_size': 10},
            #Город и дата подачи
            {'text': 'applyCity', 'x': 44, 'y': 184, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyDay', 'x': 139, 'y': 184, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyMonth', 'x': 168, 'y': 184, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyYear', 'x': 246, 'y': 184, 'font': 'Helvetica', 'font_size': 10},

        ],
        'selectors': {
            # Тип Визы
            'VisaTypeSelect': {
                'Option1': {'x': 64, 'y': 570},
                'Option2': {'x': 64, 'y': 556},
                'Option3': {'x': 64, 'y': 543}
            },
            'FamilyStatusSelect': {
                'Option1': {'x': 384, 'y': 483},
                'Option2': {'x': 413, 'y': 483},
                'Option3': {'x': 441, 'y': 483},
                'Option4': {'x': 464, 'y': 483},
                'Option5': {'x': 492, 'y': 483},
                'Option6': {'x': 521, 'y': 483}
            },
            'GenderSelect': {
                'Option1': {'x': 272, 'y': 484},
                'Option2': {'x': 301, 'y': 484}
            }
       }
    },
    'MI-F Spouse': {
        'text_items': [
            # паспорт
            {'text': 'passportSpouse', 'x': 104, 'y': 842 - 351, 'font': 'Helvetica', 'font_size': 10},
            # NIE
            {'text': 'NIE1Spouse', 'x': 335, 'y': 842 - 351, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'NIE2Spouse', 'x': 366, 'y': 842 - 351, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'NIE3Spouse', 'x': 524, 'y': 842 - 351, 'font': 'Helvetica', 'font_size': 10},
            # имя и фамилия
            {'text': 'fullSurnameSpouse', 'x': 92, 'y': 842 - 364, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'fullNameSpouse', 'x': 396, 'y': 842 - 364, 'font': 'Helvetica', 'font_size': 10},

            # lugar de nacimiento
            {'text': 'cityOriginalSpouse', 'x': 126, 'y': 842 - 377, 'font': 'Helvetica', 'font_size': 10},
            # дата
            {'text': 'birthDaySpouse', 'x': 137, 'y': 842 - 391, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthMonthSpouse', 'x': 165, 'y': 842 - 391, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthYearSpouse', 'x': 191, 'y': 842 - 391, 'font': 'Helvetica', 'font_size': 10},
            # страна и национальность
            {'text': 'birthCountrySpouse', 'x': 252, 'y': 842 - 391, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'NacinalidadSpouse', 'x': 444, 'y': 842 - 391, 'font': 'Helvetica', 'font_size': 10},
            # имя папы и мамы
            {'text': 'namePapaSpouse', 'x': 126, 'y': 842 - 404, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'nameMamaSpouse', 'x': 381, 'y': 842 - 404, 'font': 'Helvetica', 'font_size': 10},
            # адрес - улица
            {'text': 'adressStreetSpouse', 'x': 126, 'y': 842 - 417, 'font': 'Helvetica', 'font_size': 10},
            # адрес - дом и квартира
            {'text': 'adressBuildingSpouse', 'x': 485, 'y': 842 - 417, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressFlatSpouse', 'x': 527, 'y': 842 - 417, 'font': 'Helvetica', 'font_size': 10},
            # Licalidad
            {'text': 'citySpainSpouse', 'x': 92, 'y': 842 - 430, 'font': 'Helvetica', 'font_size': 10},
            # CP и провинция
            {'text': 'indexSpainSpouse', 'x': 318, 'y': 842 - 430, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'provinciaSpainSpouse', 'x': 418, 'y': 842 - 430, 'font': 'Helvetica', 'font_size': 10},
            # телефон и емейл
            {'text': 'telephonSpainSpouse', 'x': 132, 'y': 842 - 454, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'emailSpouse', 'x': 330, 'y': 842 - 454, 'font': 'Helvetica', 'font_size': 10},
            # numero de referancial completo
            {'text': 'numRefCompSpouse', 'x': 417, 'y': 842 - 636, 'font': 'Helvetica', 'font_size': 10},
            # Город и дата подачи
            {'text': 'applyCitySpouse', 'x': 42, 'y': 842 - 669, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyDaySpouse', 'x': 140, 'y': 842 - 669, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyMonthSpouse', 'x': 164, 'y': 842 - 669, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyYearSpouse', 'x': 248, 'y': 842 - 669, 'font': 'Helvetica', 'font_size': 10},

            # Данные основого аппликанта
            {'text': 'mainApplicantMumRegSilicitudSpouse', 'x': 288, 'y': 842 - 519, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'mainApplicantPassportSpouse', 'x': 105, 'y': 842 - 529, 'font': 'Helvetica', 'font_size': 10},

            {'text': 'mainApplicantNIE1Spouse', 'x': 323, 'y': 842 - 529, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'mainApplicantNIE2Spouse', 'x': 349, 'y': 842 - 529, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'mainApplicantNIE3Spouse', 'x': 520, 'y': 842 - 529, 'font': 'Helvetica', 'font_size': 10},

            {'text': 'mainApplicantSurnameSpouse', 'x': 92, 'y': 842 - 542, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'mainApplicantNameSpouse', 'x': 381, 'y': 842 - 542, 'font': 'Helvetica', 'font_size': 10}


        ],
        'selectors': {
            # Тип Визы
            'VisaTypeSelectSpouse': {
                'Option1': {'x': 65, 'y': 842 - 274},
                'Option2': {'x': 65, 'y': 842 - 288},
                'Option3': {'x': 65, 'y': 842 - 301}
            },
            'FamilyStatusSelectSpouse': {
                'Option1': {'x': 384, 'y': 842 - 377},
                'Option2': {'x': 411, 'y': 842 - 377},
                'Option3': {'x': 439, 'y': 842 - 377},
                'Option4': {'x': 463, 'y': 842 - 377},
                'Option5': {'x': 492, 'y': 842 - 377},
                'Option6': {'x': 521, 'y': 842 - 377}
            },
            'GenderSelectSpouse': {
                'Option1': {'x': 272, 'y': 842 - 377},
                'Option2': {'x': 302, 'y': 842 - 377}
            },
            'FamilyRelationSelectSpouse': {
                'Option1': {'x':103, 'y': 842 - 481},
                'Option2': {'x': 155, 'y': 842 - 481},
                'Option3': {'x': 231, 'y': 842 - 481},
                'Option4': {'x': 357, 'y': 842 - 481},
                'Option5': {'x': 475, 'y': 842 - 481}
            },
        }
    },
    'MI-F Child': {
        'text_items': [
            # паспорт
            {'text': 'passportChild', 'x': 104, 'y': 842 - 351, 'font': 'Helvetica', 'font_size': 10},
            # NIE
            {'text': 'NIE1Child', 'x': 335, 'y': 842 - 351, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'NIE2Child', 'x': 366, 'y': 842 - 351, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'NIE3Child', 'x': 524, 'y': 842 - 351, 'font': 'Helvetica', 'font_size': 10},
            # имя и фамилия
            {'text': 'fullSurnameChild', 'x': 92, 'y': 842 - 364, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'fullNameChild', 'x': 396, 'y': 842 - 364, 'font': 'Helvetica', 'font_size': 10},

            # lugar de nacimiento
            {'text': 'cityOriginalChild', 'x': 126, 'y': 842 - 377, 'font': 'Helvetica', 'font_size': 10},
            # дата
            {'text': 'birthDayChild', 'x': 137, 'y': 842 - 391, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthMonthChild', 'x': 165, 'y': 842 - 391, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthYearChild', 'x': 191, 'y': 842 - 391, 'font': 'Helvetica', 'font_size': 10},
            # страна и национальность
            {'text': 'birthCountryChild', 'x': 252, 'y': 842 - 391, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'NacinalidadChild', 'x': 444, 'y': 842 - 391, 'font': 'Helvetica', 'font_size': 10},
            # имя папы и мамы
            {'text': 'namePapaChild', 'x': 126, 'y': 842 - 404, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'nameMamaChild', 'x': 381, 'y': 842 - 404, 'font': 'Helvetica', 'font_size': 10},
            # адрес - улица
            {'text': 'adressStreetChild', 'x': 126, 'y': 842 - 417, 'font': 'Helvetica', 'font_size': 10},
            # адрес - дом и квартира
            {'text': 'adressBuildingChild', 'x': 485, 'y': 842 - 417, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressFlatChild', 'x': 527, 'y': 842 - 417, 'font': 'Helvetica', 'font_size': 10},
            # Licalidad
            {'text': 'citySpainChild', 'x': 92, 'y': 842 - 430, 'font': 'Helvetica', 'font_size': 10},
            # CP и провинция
            {'text': 'indexSpainChild', 'x': 318, 'y': 842 - 430, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'provinciaSpainChild', 'x': 418, 'y': 842 - 430, 'font': 'Helvetica', 'font_size': 10},
            # телефон и емейл
            {'text': 'telephonSpainChild', 'x': 132, 'y': 842 - 454, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'emailChild', 'x': 330, 'y': 842 - 454, 'font': 'Helvetica', 'font_size': 10},
            # numero de referancial completo
            {'text': 'numRefCompChild', 'x': 417, 'y': 842 - 636, 'font': 'Helvetica', 'font_size': 10},
            # Город и дата подачи
            {'text': 'applyCityChild', 'x': 42, 'y': 842 - 669, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyDayChild', 'x': 140, 'y': 842 - 669, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyMonthChild', 'x': 164, 'y': 842 - 669, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyYearChild', 'x': 248, 'y': 842 - 669, 'font': 'Helvetica', 'font_size': 10},

            # Данные основого аппликанта
            {'text': 'mainApplicantMumRegSilicitudChild', 'x': 288, 'y': 842 - 519, 'font': 'Helvetica',
             'font_size': 10},
            {'text': 'mainApplicantPassportChild', 'x': 105, 'y': 842 - 529, 'font': 'Helvetica', 'font_size': 10},

            {'text': 'mainApplicantNIE1Child', 'x': 323, 'y': 842 - 529, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'mainApplicantNIE2Child', 'x': 349, 'y': 842 - 529, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'mainApplicantNIE3Child', 'x': 520, 'y': 842 - 529, 'font': 'Helvetica', 'font_size': 10},

            {'text': 'mainApplicantSurnameChild', 'x': 92, 'y': 842 - 542, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'mainApplicantNameChild', 'x': 381, 'y': 842 - 542, 'font': 'Helvetica', 'font_size': 10},

            # Данные представителя
            {
                'keys': ['surNameChildRep', 'nameChildRep'],
                'format': '{} {}',  # Формат с пробелом между именем и фамилией
                'x': 168, 'y': 842 - 467, 'font': 'Helvetica', 'font_size': 10
            },
            {'text': 'passNameChildRep', 'x': 470, 'y': 842 - 467, 'font': 'Helvetica', 'font_size': 10}

        ],
        'selectors': {
            # Тип Визы
            'VisaTypeSelectChild': {
                'Option1': {'x': 65, 'y': 842 - 274},
                'Option2': {'x': 65, 'y': 842 - 288},
                'Option3': {'x': 65, 'y': 842 - 301}
            },
            'FamilyStatusSelectChild': {
                'Option1': {'x': 384, 'y': 842 - 377},
                'Option2': {'x': 411, 'y': 842 - 377},
                'Option3': {'x': 439, 'y': 842 - 377},
                'Option4': {'x': 463, 'y': 842 - 377},
                'Option5': {'x': 492, 'y': 842 - 377},
                'Option6': {'x': 521, 'y': 842 - 377}
            },
            'GenderSelectChild': {
                'Option1': {'x': 272, 'y': 842 - 377},
                'Option2': {'x': 302, 'y': 842 - 377}
            },
            'FamilyRelationSelectChild': {
                'Option1': {'x': 103, 'y': 842 - 481},
                'Option2': {'x': 155, 'y': 842 - 481},
                'Option3': {'x': 231, 'y': 842 - 481},
                'Option4': {'x': 357, 'y': 842 - 481},
                'Option5': {'x': 475, 'y': 842 - 481}
            },
        }
    },

    'DESIGNACION DE REPRESENTANTE':  {
        'text_items': [
        #имя, фамилия
        {'text': 'fullName', 'x': 66, 'y': 842-188, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'fullSurname', 'x': 260, 'y': 842-188, 'font': 'Helvetica', 'font_size': 10},
        #национальность, NIE, Pasaporte
        {'text': 'Nacinalidad', 'x': 82, 'y': 842-207, 'font': 'Helvetica', 'font_size': 10},
        {
            'keys': ['NIE1', 'NIE2','NIE3'],
            'format': '{}{}{}',  # Формат с пробелом между именем и фамилией
            'x': 280, 'y': 842-207, 'font': 'Helvetica', 'font_size': 12
        },
        {'text': 'passport', 'x': 462, 'y': 842-207, 'font': 'Helvetica', 'font_size': 10},

        # Дата рождения
        {'text': 'birthDay', 'x': 107, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'birthMonth', 'x': 151, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'birthYear', 'x': 192, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},

        # локалидаль, страна
        {'text': 'cityOriginal', 'x': 258, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'birthCountry', 'x': 443, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},

        # Падре, Мадре
        {'text': 'namePapa', 'x': 97, 'y': 842 - 242, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'nameMama', 'x': 285, 'y': 842 - 242, 'font': 'Helvetica', 'font_size': 10},

        # улица/дом/квартира
        {'text': 'adressStreet', 'x': 108, 'y': 842 - 259, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'adressBuilding', 'x': 487, 'y': 842 - 259, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'adressFlat', 'x': 538, 'y': 842 - 259, 'font': 'Helvetica', 'font_size': 10},

        # локаль/cp/провинция
        {'text': 'citySpain', 'x': 68, 'y': 842 - 277, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'indexSpain', 'x': 386, 'y': 842 - 277, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'provinciaSpain', 'x': 457, 'y': 842 - 277, 'font': 'Helvetica', 'font_size': 10},

        # телефон/емейл
        {'text': 'telephonSpain', 'x': 68, 'y': 842 - 292, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'email', 'x': 300, 'y': 842 - 292, 'font': 'Helvetica', 'font_size': 10},

        # город подачи
        {'text': 'applyCity', 'x': 218, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},
        # дата подачи
        {'text': 'applyDay', 'x': 293, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'applyMonth', 'x': 322, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},
        {'text': 'applyYear', 'x': 399, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},

    ],
        'selectors': {
            'FamilyStatusSelect': {
                'Option1': {'x': 451, 'y': 601},
                'Option2': {'x': 472, 'y': 842 - 241},
                'Option3': {'x': 493, 'y': 842 - 241},
                'Option4': {'x': 515, 'y': 842 - 241},
                'Option5': {'x': 546, 'y': 842 - 241},
                'Option6': {'x': 472, 'y': 842 - 241}
            }
       }
    },
    'DESIGNACION DE REPRESENTANTE Spouse': {
        'text_items': [
            # имя, фамилия
            {'text': 'fullNameSpouse', 'x': 66, 'y': 842 - 188, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'fullSurnameSpouse', 'x': 260, 'y': 842 - 188, 'font': 'Helvetica', 'font_size': 10},
            # национальность, NIE, Pasaporte
            {'text': 'NacinalidadSpouse', 'x': 82, 'y': 842 - 207, 'font': 'Helvetica', 'font_size': 10},
            {
                'keys': ['NIE1Spouse', 'NIE2Spouse', 'NIE3Spouse'],
                'format': '{}{}{}',  # Формат с пробелом между именем и фамилией
                'x': 280, 'y': 842 - 207, 'font': 'Helvetica', 'font_size': 12
            },
            {'text': 'passportSpouse', 'x': 462, 'y': 842 - 207, 'font': 'Helvetica', 'font_size': 10},

            # Дата рождения
            {'text': 'birthDaySpouse', 'x': 107, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthMonthSpouse', 'x': 151, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthYearSpouse', 'x': 192, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},

            # локалидаль, страна
            {'text': 'cityOriginalSpouse', 'x': 258, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthCountrySpouse', 'x': 443, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},

            # Падре, Мадре
            {'text': 'namePapaSpouse', 'x': 97, 'y': 842 - 242, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'nameMamaSpouse', 'x': 285, 'y': 842 - 242, 'font': 'Helvetica', 'font_size': 10},

            # улица/дом/квартира
            {'text': 'adressStreetSpouse', 'x': 108, 'y': 842 - 259, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressBuildingSpouse', 'x': 487, 'y': 842 - 259, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressFlatSpouse', 'x': 538, 'y': 842 - 259, 'font': 'Helvetica', 'font_size': 10},

            # локаль/cp/провинция
            {'text': 'citySpainSpouse', 'x': 68, 'y': 842 - 277, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'indexSpainSpouse', 'x': 386, 'y': 842 - 277, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'provinciaSpainSpouse', 'x': 457, 'y': 842 - 277, 'font': 'Helvetica', 'font_size': 10},

            # телефон/емейл
            {'text': 'telephonSpainSpouse', 'x': 68, 'y': 842 - 292, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'emailSpouse', 'x': 300, 'y': 842 - 292, 'font': 'Helvetica', 'font_size': 10},

            # город подачи
            {'text': 'applyCitySpouse', 'x': 218, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},
            # дата подачи
            {'text': 'applyDaySpouse', 'x': 293, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyMonthSpouse', 'x': 322, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyYearSpouse', 'x': 399, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},

        ],
        'selectors': {
            'FamilyStatusSelectSpouse': {
                'Option1': {'x': 451, 'y': 601},
                'Option2': {'x': 472, 'y': 842 - 241},
                'Option3': {'x': 493, 'y': 842 - 241},
                'Option4': {'x': 515, 'y': 842 - 241},
                'Option5': {'x': 546, 'y': 842 - 241},
                'Option6': {'x': 472, 'y': 842 - 241}
            }
        }
    },
    'DESIGNACION DE REPRESENTANTE Child': {
        'text_items': [
            # имя, фамилия
            {'text': 'fullNameChild', 'x': 66, 'y': 842 - 188, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'fullSurnameChild', 'x': 260, 'y': 842 - 188, 'font': 'Helvetica', 'font_size': 10},
            # национальность, NIE, Pasaporte
            {'text': 'NacinalidadChild', 'x': 82, 'y': 842 - 207, 'font': 'Helvetica', 'font_size': 10},
            {
                'keys': ['NIE1Child', 'NIE2Child', 'NIE3Child'],
                'format': '{}{}{}',  # Формат с пробелом между именем и фамилией
                'x': 280, 'y': 842 - 207, 'font': 'Helvetica', 'font_size': 12
            },
            {'text': 'passportChild', 'x': 462, 'y': 842 - 207, 'font': 'Helvetica', 'font_size': 10},

            # Дата рождения
            {'text': 'birthDayChild', 'x': 107, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthMonthChild', 'x': 151, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthYearChild', 'x': 192, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},

            # локалидаль, страна
            {'text': 'cityOriginalChild', 'x': 258, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthCountryChild', 'x': 443, 'y': 842 - 226, 'font': 'Helvetica', 'font_size': 10},

            # Падре, Мадре
            {'text': 'namePapaChild', 'x': 97, 'y': 842 - 242, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'nameMamaChild', 'x': 285, 'y': 842 - 242, 'font': 'Helvetica', 'font_size': 10},

            # улица/дом/квартира
            {'text': 'adressStreetChild', 'x': 108, 'y': 842 - 259, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressBuildingChild', 'x': 487, 'y': 842 - 259, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressFlatChild', 'x': 538, 'y': 842 - 259, 'font': 'Helvetica', 'font_size': 10},

            # локаль/cp/провинция
            {'text': 'citySpainChild', 'x': 68, 'y': 842 - 277, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'indexSpainChild', 'x': 386, 'y': 842 - 277, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'provinciaSpainChild', 'x': 457, 'y': 842 - 277, 'font': 'Helvetica', 'font_size': 10},

            # телефон/емейл
            {'text': 'telephonSpainChild', 'x': 68, 'y': 842 - 292, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'emailChild', 'x': 300, 'y': 842 - 292, 'font': 'Helvetica', 'font_size': 10},

            # город подачи
            {'text': 'applyCityChild', 'x': 218, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},
            # дата подачи
            {'text': 'applyDayChild', 'x': 293, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyMonthChild', 'x': 322, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyYearChild', 'x': 399, 'y': 842 - 540, 'font': 'Helvetica', 'font_size': 10},

        ],
        'selectors': {
            'FamilyStatusSelectChild': {
                'Option1': {'x': 451, 'y': 601},
                'Option2': {'x': 472, 'y': 842 - 241},
                'Option3': {'x': 493, 'y': 842 - 241},
                'Option4': {'x': 515, 'y': 842 - 241},
                'Option5': {'x': 546, 'y': 842 - 241},
                'Option6': {'x': 472, 'y': 842 - 241}
            }
        }
    },

    'DECLARACION DE ENTRADA': {
        'text_items': [
            # имя и фамилия
            {'text': 'fullName', 'x': 64, 'y': 842-214, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'fullSurname', 'x': 255, 'y': 842-214, 'font': 'Helvetica', 'font_size': 10},

            # национальность
            {'text': 'Nacinalidad', 'x': 77, 'y': 842-232, 'font': 'Helvetica', 'font_size': 10},

            # NIE
            {
                'keys': ['NIE1', 'NIE2', 'NIE3'],
                'format': '{}{}{}',
                'x': 275, 'y': 842-232, 'font': 'Helvetica', 'font_size': 12
            },

            # паспорт
            {'text': 'passport', 'x': 458, 'y': 842-232, 'font': 'Helvetica', 'font_size': 10},

            # дата рождения
            {'text': 'birthDay', 'x': 105, 'y': 842-250, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthMonth', 'x': 148, 'y': 842-250, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthYear', 'x': 190, 'y': 842-250, 'font': 'Helvetica', 'font_size': 10},

            # lugar de nacimiento
            {'text': 'cityOriginal', 'x': 255, 'y': 842-250, 'font': 'Helvetica', 'font_size': 10},

            # страна
            {'text': 'birthCountry', 'x': 440, 'y': 842-250, 'font': 'Helvetica', 'font_size': 10},

            #имя папы и мамы
            {'text': 'namePapa', 'x': 91, 'y': 842-267, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'nameMama', 'x': 281, 'y': 842-267, 'font': 'Helvetica', 'font_size': 10},

            #адрес - улица
            {'text': 'adressStreet', 'x': 100, 'y': 842-284, 'font': 'Helvetica', 'font_size': 10},

            #адрес - дом и квартира
            {'text': 'adressBuilding', 'x': 485, 'y': 842-284, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressFlat', 'x': 535, 'y': 842-284, 'font': 'Helvetica', 'font_size': 10},

            #Licalidad
            {'text': 'citySpain', 'x': 67, 'y': 842-301, 'font': 'Helvetica', 'font_size': 10},

            #CP и провинция
            {'text': 'indexSpain', 'x': 378, 'y': 842-301, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'provinciaSpain', 'x': 456, 'y': 842-301, 'font': 'Helvetica', 'font_size': 10},

            #телефон и емейл
            {'text': 'telephonSpain', 'x': 67, 'y': 842-317, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'email', 'x': 298, 'y': 842-317, 'font': 'Helvetica', 'font_size': 10},

            # дата въезда в испанию
            {'text': 'comingDay', 'x': 312, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'comingMonth', 'x': 340, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'comingYear', 'x': 368, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},
            # из какой страны приехал
            {'text': 'comingFrom', 'x': 470, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},

            #Город и дата получения деклорации о въезде
            {'text': 'entradaCity', 'x': 239, 'y': 842-551, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'entradaDay', 'x': 314, 'y': 842-551, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'entradaMonth', 'x': 340, 'y': 842-551, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'entradaYear', 'x': 410, 'y': 842-551, 'font': 'Helvetica', 'font_size': 10},

        ],
        'selectors': {
            'FamilyStatusSelect': {
                'Option1': {'x': 449, 'y': 842-267},
                'Option2': {'x': 470, 'y': 842-267},
                'Option3': {'x': 491, 'y': 842-267},
                'Option4': {'x': 513, 'y': 842-267},
                'Option5': {'x': 544, 'y': 842-267},
                'Option6': {'x': 470, 'y': 842-267}
            },
       }
    },
    'DECLARACION DE ENTRADA Spouse': {
        'text_items': [
            # имя и фамилия
            {'text': 'fullNameSpouse', 'x': 64, 'y': 842 - 214, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'fullSurnameSpouse', 'x': 255, 'y': 842 - 214, 'font': 'Helvetica', 'font_size': 10},

            # национальность
            {'text': 'NacinalidadSpouse', 'x': 77, 'y': 842 - 232, 'font': 'Helvetica', 'font_size': 10},

            # NIE
            {
                'keys': ['NIE1Spouse', 'NIE2Spouse', 'NIE3Spouse'],
                'format': '{}{}{}',
                'x': 275, 'y': 842 - 232, 'font': 'Helvetica', 'font_size': 12
            },

            # паспорт
            {'text': 'passportSpouse', 'x': 458, 'y': 842 - 232, 'font': 'Helvetica', 'font_size': 10},

            # дата рождения
            {'text': 'birthDaySpouse', 'x': 105, 'y': 842 - 250, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthMonthSpouse', 'x': 148, 'y': 842 - 250, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthYearSpouse', 'x': 190, 'y': 842 - 250, 'font': 'Helvetica', 'font_size': 10},

            # lugar de nacimiento
            {'text': 'cityOriginalSpouse', 'x': 255, 'y': 842 - 250, 'font': 'Helvetica', 'font_size': 10},

            # страна
            {'text': 'birthCountrySpouse', 'x': 440, 'y': 842 - 250, 'font': 'Helvetica', 'font_size': 10},

            # имя папы и мамы
            {'text': 'namePapaSpouse', 'x': 91, 'y': 842 - 267, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'nameMamaSpouse', 'x': 281, 'y': 842 - 267, 'font': 'Helvetica', 'font_size': 10},

            # адрес - улица
            {'text': 'adressStreetSpouse', 'x': 100, 'y': 842 - 284, 'font': 'Helvetica', 'font_size': 10},

            # адрес - дом и квартира
            {'text': 'adressBuildingSpouse', 'x': 485, 'y': 842 - 284, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressFlatSpouse', 'x': 535, 'y': 842 - 284, 'font': 'Helvetica', 'font_size': 10},

            # Licalidad
            {'text': 'citySpainSpouse', 'x': 67, 'y': 842 - 301, 'font': 'Helvetica', 'font_size': 10},

            # CP и провинция
            {'text': 'indexSpainSpouse', 'x': 378, 'y': 842 - 301, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'provinciaSpainSpouse', 'x': 456, 'y': 842 - 301, 'font': 'Helvetica', 'font_size': 10},

            # телефон и емейл
            {'text': 'telephonSpainSpouse', 'x': 67, 'y': 842 - 317, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'emailSpouse', 'x': 298, 'y': 842 - 317, 'font': 'Helvetica', 'font_size': 10},

            # дата въезда в испанию
            {'text': 'comingDaySpouse', 'x': 312, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'comingMonthSpouse', 'x': 340, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'comingYearSpouse', 'x': 368, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},
            # из какой страны приехал
            {'text': 'comingFromSpouse', 'x': 470, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},

            # Город и дата получения деклорации о въезде
            {'text': 'entradaCitySpouse', 'x': 239, 'y': 842 - 551, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'entradaDaySpouse', 'x': 314, 'y': 842 - 551, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'entradaMonthSpouse', 'x': 340, 'y': 842 - 551, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'entradaYearSpouse', 'x': 410, 'y': 842 - 551, 'font': 'Helvetica', 'font_size': 10},

        ],
        'selectors': {
            'FamilyStatusSelectSpouse': {
                'Option1': {'x': 449, 'y': 842 - 267},
                'Option2': {'x': 470, 'y': 842 - 267},
                'Option3': {'x': 491, 'y': 842 - 267},
                'Option4': {'x': 513, 'y': 842 - 267},
                'Option5': {'x': 544, 'y': 842 - 267},
                'Option6': {'x': 470, 'y': 842 - 267}
            },
        }
    },
    'DECLARACION DE ENTRADA Child': {
        'text_items': [
            # имя и фамилия
            {'text': 'fullNameChild', 'x': 64, 'y': 842 - 214, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'fullSurnameChild', 'x': 255, 'y': 842 - 214, 'font': 'Helvetica', 'font_size': 10},

            # национальность
            {'text': 'NacinalidadChild', 'x': 77, 'y': 842 - 232, 'font': 'Helvetica', 'font_size': 10},

            # NIE
            {
                'keys': ['NIE1Child', 'NIE2Child', 'NIE3Child'],
                'format': '{}{}{}',
                'x': 275, 'y': 842 - 232, 'font': 'Helvetica', 'font_size': 12
            },

            # паспорт
            {'text': 'passportChild', 'x': 458, 'y': 842 - 232, 'font': 'Helvetica', 'font_size': 10},

            # дата рождения
            {'text': 'birthDayChild', 'x': 105, 'y': 842 - 250, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthMonthChild', 'x': 148, 'y': 842 - 250, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthYearChild', 'x': 190, 'y': 842 - 250, 'font': 'Helvetica', 'font_size': 10},

            # lugar de nacimiento
            {'text': 'cityOriginalChild', 'x': 255, 'y': 842 - 250, 'font': 'Helvetica', 'font_size': 10},

            # страна
            {'text': 'birthCountryChild', 'x': 440, 'y': 842 - 250, 'font': 'Helvetica', 'font_size': 10},

            # имя папы и мамы
            {'text': 'namePapaChild', 'x': 91, 'y': 842 - 267, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'nameMamaChild', 'x': 281, 'y': 842 - 267, 'font': 'Helvetica', 'font_size': 10},

            # адрес - улица
            {'text': 'adressStreetChild', 'x': 100, 'y': 842 - 284, 'font': 'Helvetica', 'font_size': 10},

            # адрес - дом и квартира
            {'text': 'adressBuildingChild', 'x': 485, 'y': 842 - 284, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressFlatChild', 'x': 535, 'y': 842 - 284, 'font': 'Helvetica', 'font_size': 10},

            # Licalidad
            {'text': 'citySpainChild', 'x': 67, 'y': 842 - 301, 'font': 'Helvetica', 'font_size': 10},

            # CP и провинция
            {'text': 'indexSpainChild', 'x': 378, 'y': 842 - 301, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'provinciaSpainChild', 'x': 456, 'y': 842 - 301, 'font': 'Helvetica', 'font_size': 10},

            # телефон и емейл
            {'text': 'telephonSpainChild', 'x': 67, 'y': 842 - 317, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'emailChild', 'x': 298, 'y': 842 - 317, 'font': 'Helvetica', 'font_size': 10},

            # дата въезда в испанию
            {'text': 'comingDayChild', 'x': 312, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'comingMonthChild', 'x': 340, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'comingYearChild', 'x': 368, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},
            # из какой страны приехал
            {'text': 'comingFromChild', 'x': 470, 'y': 842 - 386, 'font': 'Helvetica', 'font_size': 10},

            # Город и дата получения деклорации о въезде
            {'text': 'entradaCityChild', 'x': 239, 'y': 842 - 551, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'entradaDayChild', 'x': 314, 'y': 842 - 551, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'entradaMonthChild', 'x': 340, 'y': 842 - 551, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'entradaYearChild', 'x': 410, 'y': 842 - 551, 'font': 'Helvetica', 'font_size': 10},

            # Данные представителя
            {
                'keys': ['surNameChildRep', 'nameChildRep'],
                'format': '{} {}',  # Формат с пробелом между именем и фамилией
                'x': 133, 'y': 842 - 330, 'font': 'Helvetica', 'font_size': 10
            },
            {'text': 'passNameChildRep', 'x': 412, 'y': 842 - 330, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'relationChildRoRep', 'x': 500, 'y': 842 - 330, 'font': 'Helvetica', 'font_size': 10}

        ],
        'selectors': {
            'FamilyStatusSelectChild': {
                'Option1': {'x': 449, 'y': 842 - 267},
                'Option2': {'x': 470, 'y': 842 - 267},
                'Option3': {'x': 491, 'y': 842 - 267},
                'Option4': {'x': 513, 'y': 842 - 267},
                'Option5': {'x': 544, 'y': 842 - 267},
                'Option6': {'x': 470, 'y': 842 - 267}
            }
        }
    },

    'DECLARACION DE MANTENIMIENTO Spouse': {
        'text_items': [
            # имя, фамилия
            {'text': 'fullName', 'x': 64, 'y': 842 - 262, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'fullSurname', 'x': 255, 'y': 842 - 262, 'font': 'Helvetica', 'font_size': 10},
            # национальность, NIE, Pasaporte
            {'text': 'Nacinalidad', 'x': 78, 'y': 842 - 279, 'font': 'Helvetica', 'font_size': 10},
            {
                'keys': ['NIE1', 'NIE2', 'NIE3'],
                'format': '{}{}{}',  # Формат с пробелом между именем и фамилией
                'x': 276, 'y': 842 - 279, 'font': 'Helvetica', 'font_size': 12
            },
            {'text': 'passport', 'x': 458, 'y': 842 - 279, 'font': 'Helvetica', 'font_size': 10},

            # Дата рождения
            {'text': 'birthDay', 'x': 106, 'y': 842 - 297, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthMonth', 'x': 149, 'y': 842 - 297, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthYear', 'x': 192, 'y': 842 - 297, 'font': 'Helvetica', 'font_size': 10},

            # локалидаль, страна
            {'text': 'cityOriginal', 'x': 255, 'y': 842 - 297, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthCountry', 'x': 440, 'y': 842 - 297, 'font': 'Helvetica', 'font_size': 10},

            # Падре, Мадре
            {'text': 'namePapa', 'x': 94, 'y': 842 - 315, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'nameMama', 'x': 284, 'y': 842 - 315, 'font': 'Helvetica', 'font_size': 10},

            # улица/дом/квартира
            {'text': 'adressStreet', 'x': 99, 'y': 842 - 331, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressBuilding', 'x': 486, 'y': 842 - 331, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressFlat', 'x': 537, 'y': 842 - 331, 'font': 'Helvetica', 'font_size': 10},

            # локаль/cp/провинция
            {'text': 'citySpain', 'x': 68, 'y': 842 - 348, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'indexSpain', 'x': 380, 'y': 842 - 348, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'provinciaSpain', 'x': 458, 'y': 842 - 348, 'font': 'Helvetica', 'font_size': 10},

            # телефон/емейл
            {'text': 'telephonSpain', 'x': 68, 'y': 842 - 364, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'email', 'x': 298, 'y': 842 - 364, 'font': 'Helvetica', 'font_size': 10},

            # имя и фамилия супруга
            {
                'keys': ['fullNameSpouse', 'fullSurnameSpouse'],
                'format': '{} {}',  # Формат с пробелом между именем и фамилией
                'x': 216, 'y': 842 - 436, 'font': 'Helvetica', 'font_size': 12
            },


            # город подачи
            {'text': 'applyCitySpouse', 'x': 238, 'y': 842 - 559, 'font': 'Helvetica', 'font_size': 10},
            # дата подачи
            {'text': 'applyDaySpouse', 'x': 313, 'y': 842 - 559, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyMonthSpouse', 'x': 339, 'y': 842 - 559, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyYearSpouse', 'x': 408, 'y': 842 - 559, 'font': 'Helvetica', 'font_size': 10},

        ],
        'selectors': {
            'FamilyStatusSelect': {
                'Option1': {'x': 450, 'y': 842 - 314},
                'Option2': {'x': 472, 'y': 842 - 314},
                'Option3': {'x': 493, 'y': 842 - 314},
                'Option4': {'x': 515, 'y': 842 - 314},
                'Option5': {'x': 545, 'y': 842 - 314},
                'Option6': {'x': 472, 'y': 842 - 314}
            }
        }
    },


    'Autonomo': {
        'text_items': [
            # имя, фамилия
            {'text': 'fullName', 'x': 64, 'y': 842 - 249, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'fullSurname', 'x': 254, 'y': 842 - 249, 'font': 'Helvetica', 'font_size': 10},
            # национальность, NIE, Pasaporte
            {'text': 'Nacinalidad', 'x': 77, 'y': 842 - 268, 'font': 'Helvetica', 'font_size': 10},
            {
                'keys': ['NIE1', 'NIE2', 'NIE3'],
                'format': '{}{}{}',  # Формат с пробелом между именем и фамилией
                'x': 274, 'y': 842 - 268, 'font': 'Helvetica', 'font_size': 12
            },
            {'text': 'passport', 'x': 458, 'y': 842 - 268, 'font': 'Helvetica', 'font_size': 10},

            # Дата рождения
            {'text': 'birthDay', 'x': 105, 'y': 842 - 286, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthMonth', 'x': 147, 'y': 842 - 286, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthYear', 'x': 191, 'y': 842 - 286, 'font': 'Helvetica', 'font_size': 10},

            # локалидаль, страна
            {'text': 'cityOriginal', 'x': 254, 'y': 842 - 286, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'birthCountry', 'x': 448, 'y': 842 - 286, 'font': 'Helvetica', 'font_size': 10},

            # Падре, Мадре
            {'text': 'namePapa', 'x': 93, 'y': 842 - 303, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'nameMama', 'x': 281, 'y': 842 - 303, 'font': 'Helvetica', 'font_size': 10},

            # улица/дом/квартира
            {'text': 'adressStreet', 'x': 100, 'y': 842 - 320, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressBuilding', 'x': 484, 'y': 842 - 320, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'adressFlat', 'x': 535, 'y': 842 - 320, 'font': 'Helvetica', 'font_size': 10},

            # локаль/cp/провинция
            {'text': 'citySpain', 'x': 64, 'y': 842 - 335, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'indexSpain', 'x': 377, 'y': 842 - 335, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'provinciaSpain', 'x': 452, 'y': 842 - 335, 'font': 'Helvetica', 'font_size': 10},

            # телефон/емейл
            {'text': 'telephonSpain', 'x': 66, 'y': 842 - 352, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'email', 'x': 295, 'y': 842 - 352, 'font': 'Helvetica', 'font_size': 10},

            # город подачи
            {'text': 'applyCity', 'x': 218, 'y': 842 - 641, 'font': 'Helvetica', 'font_size': 10},
            # дата подачи
            {'text': 'applyDay', 'x': 293, 'y': 842 - 641, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyMonth', 'x': 319, 'y': 842 - 641, 'font': 'Helvetica', 'font_size': 10},
            {'text': 'applyYear', 'x': 391, 'y': 842 - 641, 'font': 'Helvetica', 'font_size': 10},

        ],
        'selectors': {
            'FamilyStatusSelect': {
                'Option1': {'x': 449, 'y': 842 - 303},
                'Option2': {'x': 470, 'y': 842 - 303},
                'Option3': {'x': 491, 'y': 842 - 303},
                'Option4': {'x': 512, 'y': 842 - 303},
                'Option5': {'x': 452, 'y': 842 - 303},
                'Option6': {'x': 470, 'y': 842 - 303}
            }
        }
    },
    'RETA': {

        'text_items': [
            {
                'keys': ['NavesSelect', 'fullName', 'fullSurname'],
                'format': 'Asimismo, les informo que {} {} {} se registrara en el RETA',
                'x': 73, 'y': 842-226, 'font': 'Helvetica', 'font_size': 12
            },
            {
                'keys': ['NavesSelect', 'fullName', 'fullSurname','applyCity',
                         'applyDay', 'applyMonth', 'applyYear'],
                'format': '{} {} {}, {}, {} de {} de {}',  # Формат с запятыми
                'x': 72, 'y': 842-355, 'font': 'Helvetica', 'font_size': 12
            },

            ],
        },
}
def get_template_details(template_name):
    return templates_details.get(template_name, {})
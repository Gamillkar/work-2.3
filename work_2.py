



documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "10006"}
]


def name():
    try:
        for docs in documents:
            for key, values in docs.items():
                if key == 'name':
                    print(values)
            docs['name']
    except KeyError as e:
        print('В одном из полей отсутствует ключ', e)

        return values

name()
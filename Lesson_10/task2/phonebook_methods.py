import json

file_path = 'phonebook_db.json'


def get_json_object() -> dict:
    json_dict = dict()
    try:
        json_dict = json.load(open(file_path, 'r'))
    except FileNotFoundError:
        print('No such file or directory.')
    return json_dict


def get_field(json_object: dict) -> list:
    fields = []
    for i in json_object:
        for j in json_object[i]:
            fields.append(j)
        break
    return fields
    

def update(json_object: dict, data: dict, pk=None) -> bool:
    try:
        if type(data) is dict and pk is None:
            json_object.update(data)
        else:
            json_object[pk] = data
        json.dump(json_object, open(file_path, 'w'), indent=4)
        return True
    except FileNotFoundError:
        print('No such file or directory.')
        return False

    
def delete(json_object: dict, pk: str) -> bool:
    json_object.pop(pk)
    json.dump(json_object, open(file_path, 'w'), indent=4)
    return True


def get_item(json_object: dict, pk: str) -> dict:
    try:
        return json_object[pk]
    except KeyError:
        return {}


def search(json_object: dict,  field: str, key_word: str) -> list:
    result = []
    if field == 'phone_number' and key_word in [item for item in json_object]:
        result.append(key_word)
    else:
        for item in json_object:
            try:
                if json_object[item][field].lower() == key_word.lower():
                    result.append(item)
            except KeyError:
                continue
    return result


def phone_number_validator(phone_number: str):
    warn = []
    if len(phone_number) != 13:
        warn.append('Длинна номера телефона должна равняться 13 знакам')
    if not phone_number.startswith('+'):
        warn.append('Номер телефона должен начинатся с \'+\'')
    if not phone_number[1:].isdigit():
        warn.append('Номер телефона должен содержать только цифры от 0-9')
    return warn
    
    
def display(json_object: dict, pk: list = None) -> None:
    i = 0
    print('_' * 50)
    if pk is None:
        pk = [i for i in json_object]
    while i < len(pk):
        print(f'phone_number: {pk[i]}')
        items = get_item(json_object, pk[i])
        for item in items:
            print(f'{item}: {items[item]}')
        print('_' * 50)
        i += 1


if __name__ == '__main__':
    pass



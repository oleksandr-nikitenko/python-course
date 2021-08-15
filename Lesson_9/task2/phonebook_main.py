# encode = utf-8
import phonebook_methods as pm

json_object = pm.get_json_object()

while True:
    try:
        action = int(input('ТЕЛЕФОННЫЙ СПРАВОЧНИК\n1.Посмотреть все записи\n2.Новый контакт\n3.Поиск\n4.Редактировать\n'
                           '5.Удалить\n0.Выход.\n'))
    except ValueError:
        print('Не верное значение. Повторите ввод.')
        continue
    if action == 1:
        print('ВСЕ ЗАПИСИ:')
        while True:
            pm.display(json_object)
            action = input('Нажмите ENTER для выхода в предыдущее меню.\n')
            break
    elif action == 2:
        print("НОВЫЙ КОНТАКТ:")
        while True:
            phone_number = input(f'Введите phone_number: ').strip()
            if len(pm.get_item(json_object, phone_number)) != 0:
                print('Такой номм телефона уже добавлен в справочник')
                continue
            if len(pm.phone_number_validator(phone_number)) != 0:
                for warn in pm.phone_number_validator(phone_number):
                    print(warn)
                continue
            fields = pm.get_field(json_object)
            list_items = {}
            for i in fields:
                item = input(f'Введите {i}: ').strip()
                list_items[i] = item
            
            pm.update(json_object, list_items, phone_number)
            pm.display(json_object)
            action = input('Для выхода в главное меню нажмите ENTER.\n')
            break
    elif action == 3:
        print('ПОИСК:')
        while True:
            fields = ['phone_number']+pm.get_field(json_object)
            fields_str = ', '.join(fields)
            action_field = input(f'Введите название поля по которому хотите произвести поиск ({fields_str}):\n')
            if action_field not in fields:
                continue
            action_key_word = input('Введите значение по которому вы ищете:\n')
            search_result = pm.search(json_object, action_field, action_key_word)
            if len(search_result) != 0:
                pm.display(json_object, search_result)
            else:
                print('Поиск не дал результатов')
            action = input('Для выхода в главное меню нажмите ENTER.\n')
            break
    elif action == 4:
        print('РЕДАКТИРОВАНИЕ')
        while True:
            action = input('Введите номер телефона, данные по которому вы хотите изменить: ')
            dict_edit = pm.get_item(json_object, action)
            
    elif action == 5:
        print('УДАЛЕНИЕ')
        while True:
            action = input('Введите номер телефона, который вы хотите удалить: ')
            search_result = pm.search(json_object, 'phone_number', action)
            if len(search_result) != 0:
                pm.display(json_object, search_result)
                confirm = input('Подтвердите удаление: Y\n')
                if confirm.lower() == 'y':
                    pm.delete(json_object, action)
                    break
                else:
                    print('Удаление отменено.')
                    continue
                    
            else:
                print('Поиск не дал результатов')
                break
    elif action == 0:
        print('Вы покинули программу.')
        break
        
        
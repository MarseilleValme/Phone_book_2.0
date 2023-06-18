phone_book = []
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment, *_ = contact.strip().split(':')
        phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})

def save_file():
    contact = []
    result=[]
    for dictionary in phone_book:
        for value in dictionary:
            contact.append(str(dictionary[value]))  # С дикими муками пытаюсь сформировать обратно список строк для записи в файл
        result.append(':'.join(contact)+'\n')
        contact.clear()
    with open(path, 'w', encoding='UTF-8') as file: # А файл действительно нужно переоткрывать для записи или это я такой рукожоп?
        file.writelines(result)
    file.close()
    phone_book.clear()  # Дабы при повторном открытии файла не дублировать список дописыванием в самого себя


def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))
    return {'id': max(uid_list) + 1}

def add_contact(new: dict):
    smart_girl = check_id() # Перенастроил апдейт нового контакта как советовала умная девочка. 
    smart_girl.update(new)  # Терь индексы добавляемых записей становятся на место.
    phone_book.append(smart_girl)   # Ответ на вопрос "Почему неиндексируемая коллекция оказалась чуйствительна к порядку апдейта" ждём от Вас)).

def search(word: str):
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result

def change(index: int, new):
    for key, field in new.items():
        if field != '':
            phone_book[index - 1][key] = field

def delete_record(index: int):
    phone_book.pop(index-1)
    for i in range (index-1, len(phone_book)):           # Ператрахиваю нумерацию записей после удаления.
            phone_book[i]['id']=str(i+1)

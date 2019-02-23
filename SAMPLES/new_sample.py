documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

number_pull = []
for number_in_list in documents:
    number_pull.append(number_in_list['number'])
print('Список номеров документов:', list(number_pull))
print('Список доступных комманд: p, l, s, a, d, m, as')


#################################################################
# Команда 'p'
#################################################################

def doc_number_owner(doc_number):
    """
    Принимает в себя номер документа и выводит имя человека, которому принадлежит документ с найденным номером
    """
    for document in documents:
        if document['number'] == doc_number:
            print('Владелец документа:')
            return document['name']


def input_number_p():
    p = input('Введите номер документа, чтобы узнать владельца документа:')
    while p not in number_pull:
        print('Документ с таким номером отсутствует в справочнике.')
        return input_number_p()
    else:
        return p


def main_p():
    doc_number = input_number_p()
    print(doc_number_owner(doc_number))


#################################################################
# Команда 'l'
#################################################################

def document_info():
    '''
    Выводит сисок всех документов в формате:
    passport "2207 876234" Василий Гупкин
    '''
    i = 1
    for docs in documents:
        print('Документ №', i)
        i = i + 1
        print(docs['type'], '"' + docs['number'] + '"', docs['name'])


# #################################################################
# #Команда 's'
# #################################################################

def doc_number_shelf(doc_number):
    '''
    Принимает в себя номер документа и выводит номер полки,
    на которой данный документ расположен
    '''
    for shelf, docs_on_shelf in directories.items():
        if doc_number in docs_on_shelf:
            print('Номер полки с документом:')
            return shelf


def input_number_s():
    s = input('Введите номер документа, чтобы узнать номер полки:')
    while s not in number_pull:
        print('Документ с таким номером отсутствует в справочнике.')
        return input_number_s()
    else:
        return s


def main_s():
    doc_number = input_number_s()
    print(doc_number_shelf(doc_number))


# #################################################################
# #Команда 'a'
# #################################################################

def document_adding(type_of_doc, number_of_doc, owner_of_doc, shelf_of_number):
    '''
    Принимает параметры документа и вносит его в базу, а также добавляет новый
    документ на указаную пользователем полку
    '''
    try:
        document = dict()
        another_list = list()
        another_list.append(number_of_doc)
        directories[shelf_of_number] += another_list
        document['type'] = type_of_doc
        document['number'] = number_of_doc
        document['name'] = owner_of_doc
        documents.append(document)
        print('Введенный в систему документ:')
        return document, directories
    except:
        print('Вы ввели некорректные данные, попробуйте еще раз')
        main_a()


def main_a():
    type_of_doc = input('Введите тип документа:')
    number_of_doc = input('Введите номер документа:')
    owner_of_doc = input('Введите владельца документа:')
    shelf_of_number = input('Введите номер полки для документа:')
    print(document_adding(type_of_doc, number_of_doc, owner_of_doc, shelf_of_number))


# #################################################################
# # Команда 'd'
# #################################################################

def deleting_docs_func(a):
    for i, doc in enumerate(documents):
        if a in doc['number']:
            del documents[i]
    for value in directories.values():
        if a in value:
            value.remove(a)
    return print('Список документов: {}\nСписок полок: {}'.format(documents, directories))


def main_d():
    doc_to_delete = input('Введите номер документа, который необходимо удалить: ')
    while doc_to_delete not in number_pull:
        print('Документ с таким номером отсутствует в справочнике.')
        return main_d()
    return deleting_docs_func(doc_to_delete)


# #################################################################
# # Команда 'm'
# #################################################################

def moving_func(a, b):
    '''
    Принимает значение номера документа и полки, а затем перемещает указанный
    документ на указанную полку
    '''
    new_shelf_list = list()
    new_shelf_list.append(a)
    for value in directories.values():
        if a in value:
            value.remove(a)
    directories[b] += new_shelf_list
    print('Документ был перемещен')
    return print(directories)


def main_m():
    moving_doc = input('Введите номер документа, который нужно передвинуть: ')
    shelf_to_move = input('Введите номер полки, на которую необходимо переместить документ ')
    return moving_func(moving_doc, shelf_to_move)


# #################################################################
# # Команда 'as'
# #################################################################

def main_as():
    '''
    Принимает значение новой полки и добавляет ее в общий список полок
    '''
    try:
        new_shelf_number = str(int(input('Введите номер новой полки: ')))
        directories[new_shelf_number] = []
        return print(directories)
    except:
        print('Номер полки должен быть числовым значением')
        main_as()


# #################################################################
# # Функция 'main_command'
# #################################################################
def main_command():
    incomming_command = input('Введите команду:')
    if incomming_command == 'p':
        return main_p()
    elif incomming_command == 'l':
        return document_info()
    elif incomming_command == 's':
        return main_s()
    elif incomming_command == 'a':
        return main_a()
    elif incomming_command == 'd':
        return main_d()
    elif incomming_command == 'm':
        return main_m()
    elif incomming_command == 'as':
        return main_as()
    else:
        print('Введенной команды не сущствует. Нажмите ctrl+Enter чтобы попробовать еще раз.')
        return main_command()


main_command()
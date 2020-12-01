from config.configuration import db
import tools.getdata as get
import re


def insertamensaje(collection, type_chat, name_chat, name_user, message, date):
    """
    función que inserta los datos en mongo 
    """

    dict_insert = { 'Type_Chat' : f'{type_chat}',
    'Name_Chat' : f'{name_chat}',
    'Name_User' : f'{name_user}',
    'Message' : f'{message}',
    'Date' : f'{date}'}
    collection = db[f"{collection}"]
    collection.insert_one(dict_insert)

def crear_bd_chats(collection, filename, type_chat, name_chat):
    '''
    Funcion que extrae de un archivo .txt los datos de Date, User y Message de una conversacion de chat, 
    para luego agregarla a la base de datos 
    '''
    with open(f"input/{filename}", encoding="utf-8") as fname:
        for lineas in fname:
            try:
                date = re.search(r'^\d.*:\d{2} -', lineas).group()[:-2]
                name_user = re.search(r'\- [A-Z].*[a-z]: ', lineas).group()[2:-1]
                message =re.sub( r'^\d.*\- [A-Z].*[a-z]: ', '', lineas)
                message =message.rstrip()
                if get.verificacion(collection, type_chat, name_chat, name_user, message, date) == None:
                    if type_chat == 1:
                        type_chat='Individial'
                    else:
                        type_chat='Grupo'
                    insertamensaje(collection, type_chat, name_chat, name_user, message, date)
                else:
                    continue
            except:
                continue
    return 'Agregado exitosamente a la base de datos'


def insertamensaje_one(collection, type_chat, name_chat, name_user, message, date):
    '''
    Funcion que inserta un solo mensaje por usuario a la base de datos
    '''
    if get.verificacion(collection, type_chat, name_chat, name_user, message, date) == None:
        insertamensaje(collection, type_chat, name_chat, name_user, message, date)
        return 'Agregado exitosamente a la base de datos'
    else:
        return 'No se puede agregar, ya en la base de datos existe una coincidencia para todos los datos'
   

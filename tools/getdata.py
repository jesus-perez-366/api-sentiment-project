from config.configuration import db
from textblob import TextBlob
import pandas as pd
import json
import matplotlib.pyplot as plt
from flask import Flask, render_template
from io import BytesIO
import base64

def User_group(collection,type_chat, name_chat):
    """
    Hacemos una query a la base de datos para sacar los usuarios de un grupo
    """
    query = {'Type_Chat' : type_chat,
    'Name_Chat' : name_chat}
    collection = db[f"{collection}"]
    user = collection.distinct( "Name_User", query )
    return list(user)

def Message_group(collection,type_chat, name_chat):
    """
    Hacemos una query a la base de datos para sacar los mensajes de un chat
    """
    query = {'Type_Chat' : f'{type_chat}',
    'Name_Chat' : f'{name_chat}'}
    collection = db[f"{collection}"]
    all_message = collection.find(query,{"_id":0, 'Message' : 1, 'Date' : 1})
    return list(all_message)

def count_user(collection,type_chat, name_chat):
    """
    Hacemos una query a la base de datos para obtener el numero de usuarios
    """
    query = {'Type_Chat' : f'{type_chat}',
    'Name_Chat' : f'{name_chat}'}
    collection = db[f"{collection}"]
    user = collection.distinct( "Name_User", query )
    return len(list(user))


def verificacion(collection, type_chat, name_chat, name_user, message, date):
    '''
    Funcion que verifica si la data que se quiere introducir ya se encuentra en la colleccion donde la desea colocar
    '''
    query = { 'Type_Chat' : f'{type_chat}',
    'Name_Chat' : f'{name_chat}',
    'Name_User' : f'{name_user}',
    'Message' : f'{message}',
    'Date' : f'{date}'}
    collection = db[f"{collection}"]
    try: 
        return list(collection.find(query,{"_id":0}))[0]
    except:
        return None

def count_allmessage_user(collection,type_chat, name_chat):
    '''
    realiza una query y devuelve el numero de mensaje que ha realizado cada usuario
    '''
    collection = db[f"{collection}"]
    lista = collection.aggregate([
                        { '$match': {"$and": [
            {'Type_Chat':f'{type_chat}'},
            {'Name_Chat':f'{name_chat}'}
        ]}},
                        { '$group': { '_id': "$Name_User", 'total': { '$sum': 1 } } },
                        { '$sort': { 'total': -1 } }
                    ])
    return list(lista)


def Message_for_group_and_User(collection,type_chat, name_chat, name_user):
    """
    Hacemos una query  y devuelve los mensajes realizado por los usuarios indicados
    """
    query = {'Type_Chat' : f'{type_chat}',
    'Name_Chat' : f'{name_chat}',
    "Name_User": {"$in": name_user}}
    collection = db[f"{collection}"]
    all_message_user = collection.find(query,{"_id":0, 'Name_User': 1, 'Message' : 1, 'Date' : 1}).sort("Name_User", 1)
    return list(all_message_user)


def Message_for_date(collection,type_chat, name_chat, date):
    """
    Hacemos una query y devueve los mensajes realizado en ese año
    """
    query = {'Type_Chat' : f'{type_chat}',
    'Name_Chat' : f'{name_chat}',
    "Date": {"$regex": f".*{date}.*"}}
    collection = db[f"{collection}"]
    all_message_user = collection.find(query,{"_id":0, 'Name_User': 1, 'Message' : 1, 'Date' : 1}).sort("Name_User", 1)
    return list(all_message_user)


        # frases = list(collection.find(query,{"_id":0, "Type_Chat":0, "Name_Chat":0, "Message":0, "Date"}))

def sentimentAnalysis(sentence):
    '''
    funcion que analiza la polaridad de una parrafo y devuelve su valor
    '''
    blob = TextBlob(sentence)
    return (blob.sentiment[0])

def sentimentAnalysis2(sentence):
    '''
    funcion que analiza la subjetividad de una parrafo y devuelve su valor
    '''
    blob = TextBlob(sentence)
    return (blob.sentiment[1])


def Analisis_polarizacion(collection, type_chat, name_chat):
    '''
    se realiza una query para obtener los mensajes, luego se analiza la polaridad de cada mensaje y porterior 
    se realiza la media por usuario y devuelve ese valor
    '''
    query = {'Type_Chat' : f'{type_chat}',
    'Name_Chat' : f'{name_chat}'}
    collection = db[f"{collection}"]
    all = pd.DataFrame(collection.find(query,{"_id":0, 'Name_User' : 1, 'Message' : 1}))
    all['Polaridad']=all['Message'].apply(sentimentAnalysis)
    d= all.groupby('Name_User')['Polaridad'].mean()
    data=pd.DataFrame()
    data['Name']= all.Name_User.unique()
    list1 = [round(i,3) for i in d]
    data['mean'] = list1
    data = data.sort_values('mean')
    data = data.to_json(orient='records')
    return json.loads(data)

def Analisis_user(collection, type_chat, name_chat, names_user):
    '''
    se realiza una query para obtener los mensajes, luego se analiza la polaridad de cada mensaje y 
    porterior se realiza la media por usuario y devuelve ese valor pero solo de los usuarios indicadps
    '''
    Anali = Analisis_polarizacion(collection, type_chat, name_chat)
    data = pd.DataFrame(Anali)
    data = data[data.Name.isin(names_user)]
    data = data.to_json(orient='records')
    return json.loads(data)


def Analisis_subjetivo(collection, type_chat, name_chat):
    '''
    se realiza una query para obtener los mensajes, luego se analiza la subjetividad de cada mensaje y porterior 
    se realiza la media por usuario y devuelve ese valor
    '''
    query = {'Type_Chat' : f'{type_chat}',
    'Name_Chat' : f'{name_chat}'}
    collection = db[f"{collection}"]
    all = pd.DataFrame(collection.find(query,{"_id":0, 'Name_User' : 1, 'Message' : 1}))
    all['Polaridad']=all['Message'].apply(sentimentAnalysis2)
    d= all.groupby('Name_User')['Polaridad'].mean()
    data=pd.DataFrame()
    data['Name']= all.Name_User.unique()
    list1 = [round(i,3) for i in d]
    data['mean'] = list1
    data = data.sort_values('mean')
    data = data.to_json(orient='records')
    return json.loads(data)

def Analisis_user_subjetivo(collection, type_chat, name_chat, names_user):
    '''
    se realiza una query para obtener los mensajes, luego se analiza la subjetividad de cada mensaje y 
    porterior se realiza la media por usuario y devuelve ese valor pero solo de los usuarios indicadps
    '''
    Anali = Analisis_subjetivo(collection, type_chat, name_chat)
    data = pd.DataFrame(Anali)
    data = data[data.Name.isin(names_user)]
    data = data.to_json(orient='records')
    return json.loads(data)


def scatter(data):
    '''
    realiza un skatter de la polaridad o subjetividad (segun el caso) de cada usuario, 
    y ademas se proyecta una recta que inda la media de la polaridad o subjetividad en todo el chat.
     Por ultimo se representa una zona de riesgo
    '''
    img = BytesIO()
    plt.axhline(data['mean'].mean(),
        c="red",
        linewidth= 3.,
        linestyle='--',
        label='mean')
    
    plt.axhline(0,
        c="black",
        linewidth= 0.5,
        linestyle='-',
        label='neutro')


    plt.fill_between((0,len(data)),(-1),color='r', alpha=0.3, label='Alerta')
    plt.text((len(data)/2)-2, -0.8, "Alerta", size=15)
    plt.fill_between((0,len(data)),(-0.5),color='w')

    x=range(0, len(data))
    y=data['mean']
    cm = plt.cm.get_cmap('RdYlBu')
    s1 = plt.scatter(x, y, c=y, vmin=-1, vmax=1, cmap='plasma')
    plt.colorbar(s1)


    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('plot.html', plot_url=plot_url)
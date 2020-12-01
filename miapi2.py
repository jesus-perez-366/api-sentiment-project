from flask import Flask, request, render_template
from werkzeug import secure_filename
import os
import markdown.extensions.fenced_code
import json
import tools.getdata as get
import tools.postdata as pos
import pandas as pd
import markdown.extensions.fenced_code


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './input'

@app.route("/load")
def upload_file():
 # renderiamos la plantilla "formulario.html"
 return render_template('formulario.html')

@app.route("/upload", methods=['POST'])
def uploader():
 if request.method == 'POST':
  f = request.files['archivo'] # obtenemos el archivo del input "archivo"
  filename = secure_filename(f.filename)
  f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # Guardamos el archivo en el directorio "Archivos PDF"
  type_chat = request.form['Tipo_Chat']
  name_chat = request.form['nombre']
  collection = request.form['Collection']
  return pos.crear_bd_chats(collection, filename, type_chat, name_chat) # Retornamos una respuesta 

@app.route("/insertar", methods=['POST'])
def insert():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    dato3 = request.form.get('Name_User')
    dato4 = request.form.get('Message')
    dato5 = request.form.get('Date')
    return json.dumps(pos.insertamensaje_one(collection, dato1, dato2, dato3, dato4, dato5))


@app.route("/User_group", methods=['GET'])
def User():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    user = get.User_group(collection, dato1, dato2)
    return json.dumps(user)

@app.route("/User/Num", methods=['GET'])
def Num_User():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    user = get.count_user(collection, dato1, dato2)
    return json.dumps(user)

@app.route("/message", methods=['GET'])
def message():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    mes = get.Message_group(collection,dato1, dato2)
    return json.dumps(mes)

@app.route("/message/list", methods=['GET'])
def list_message():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    lis_mes = get.count_allmessage_user(collection,dato1, dato2)
    return json.dumps(lis_mes)

@app.route("/message/user", methods=['GET'])
def user_message():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    dato3 = request.form.getlist('Name_User')
    user_mes = get.Message_for_group_and_User(collection,dato1, dato2, dato3)
    return json.dumps(user_mes)

@app.route("/message/date", methods=['GET'])
def Date_message():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    dato3 = request.form.get('Date')
    user_mes = get.Message_for_date(collection,dato1, dato2, dato3)
    return json.dumps(user_mes)



@app.route("/Polaridad", methods=['GET'])
def Analisis():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    Anali = get.Analisis_polarizacion(collection, dato1, dato2)
    return json.dumps(Anali)

@app.route("/Polaridad/User", methods=['GET'])
def Analisis3():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    dato3 = request.form.getlist('Names_user')
    Anali = get.Analisis_user(collection, dato1, dato2, dato3)
    return json.dumps(Anali)


@app.route('/plot/<Collection>/<Type_Chat>/<Name_Chat>')
def plot(Collection, Type_Chat, Name_Chat):
    Anali = get.Analisis_polarizacion(Collection, Type_Chat, Name_Chat)
    data = pd.DataFrame(Anali)
    return get.scatter(data)


@app.route("/subjetividad", methods=['GET'])
def Analisis2():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    Anali = get.Analisis_subjetivo(collection, dato1, dato2)
    return json.dumps(Anali)

@app.route("/subjetividad/User", methods=['GET'])
def Analisis4():
    collection = request.form.get('Collection')
    dato1 = request.form.get('Type_Chat')
    dato2 = request.form.get('Name_Chat')
    dato3 = request.form.getlist('Names_user')
    Anali = get.Analisis_user_subjetivo(collection, dato1, dato2, dato3)
    return json.dumps(Anali)

@app.route('/plot2/<Collection>/<Type_Chat>/<Name_Chat>')
def plot2(Collection, Type_Chat, Name_Chat):
    Anali = get.Analisis_subjetivo(Collection, Type_Chat, Name_Chat)
    data = pd.DataFrame(Anali)
    return get.scatter(data)


@app.route("/readme")
def index():
    readme_file = open("README.md","r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string







app.run(debug=True)

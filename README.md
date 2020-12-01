# api-sentiment-project
Elaboracion de una API que permitira realizar metodos GET y POST a una base de datos en MongoDB, la cual presenta un formato de Chat.


## Estructura de la base de datos
### Formato diccionario

{Type_Chat : "string",

Name_Chat : "string",

Name_User : "string", 

Message : "string",

Date : "dd/mm/aa"}



## Parametro Generales para el uso de la API

Type_Chat : indicar si el chat es una Grupo o Individual

Name_Chat : Nombre del Chat,

Name_User : Nombre del Usuario, 

Message : Mensaje que ha enviado el usuario, 

Date : Fecha en que fue enviado el mensaje en el formato dd/mm/aa

Collection : NOmbre de la Coleccion de la base de datos



## Metodo GET

### 1.- Solicitudud de Usuarios presentes en el grupo

##### Endpoint = "http://localhost:5000/User_group"

#### Parametros requeridos (en forma de diccionario)

'Collection': " "

'Type_Chat': " "

'Name_Chat': " "


#### Ejemplo:

url = "http://localhost:5000/User_group"

dato = {'Type_Chat':'Grupo', 'Name_Chat':'recuvenza', 'Collection': 'chat'}

frases = requests.get(url, data=dato)

Repuesta:

```
['Carlos:',
 'Cristian:',
 'Edison:',
 'Estefan:',
 'Franco:',
 'Hermes:',
 'Latina:']

```



### 2.- Solicitudud del total de Usuarios presentes en el grupo.

##### Endpoint = "http://localhost:5000/message"

#### Parametros requeridos (en forma de diccionario)

'Collection': " "

'Type_Chat': " "

'Name_Chat': " "


#### Ejemplo:

url = "http://localhost:5000/message"

dato = {'Type_Chat':'Grupo', 'Name_Chat':'recuvenza', 'Collection': 'chat'}

frases = requests.get(url, data=dato)

Repuesta: Un numero entero 

```
20
```



### 3.- Solicitud de todos los mensajes del chat.

##### Endpoint = "http://localhost:5000/message/list"

#### Parametros requeridos (en forma de diccionario)

'Collection': " "

'Type_Chat': " "

'Name_Chat': " "


#### Ejemplo:

url = "http://localhost:5000/message/list"

dato = {'Type_Chat':'Grupo', 'Name_Chat':'recuvenza', 'Collection': 'chat'}

frases = requests.get(url, data=dato)

Repuesta:

```
[{'Message': 'Thank you brother!', 'Date': '12/21/18 15:15'},
 {'Message': '', 'Date': '12/21/18 15:21'},
 {'Message': 'Note', 'Date': '12/21/18 18:09'},
 {'Message': 'In mind', 'Date': '12/21/18 18:10'},
 {'Message': 'Good afternoon Yaritza you can count on me',
  'Date': '12/21/18 18:11'},
 {'Message': 'Thank you Yaritza, for the information',
  'Date': '12/21/18 18:11'}]
```



### 4.- Solicitud de todos los mensajes de los usuarios indicados pertenecientes a un chat.

##### Endpoint = "http://localhost:5000/message/user"

#### Parametros requeridos (en forma de diccionario)

'Collection': " "

'Type_Chat': " "

'Name_Chat': " "

'Name_User': [' ',' '] (los usurios se pasan en formato lista)


#### Ejemplo:

url = "http://localhost:5000/message/user"

dato = {'Type_Chat':'Grupo', 'Name_Chat':'recuvenza', 'Collection': 'chat', 'Name_User': ['Patricia:','Yaritza:']}

frases = requests.get(url, data=dato)

Repuesta:

```
[{'Name_User': 'Patricia:', 'Message': '', 'Date': '1/5/19 17:16'},
 {'Name_User': 'Patricia:',
  'Message': 'Good morning Pilar vanessach.6385@gmail.com',
  'Date': '5/2/19 15:49'},
 {'Name_User': 'Yaritza:', 'Message': 'Note', 'Date': '12/21/18 18:09'},
 {'Name_User': 'Yaritza:',
  'Message': 'Also available',
  'Date': '12/21/18 18:13'}]
```



### 5.- Solicitud de todos los mensajes de los usuarios indicados pertenecientes a un chat.

##### Endpoint = "http://localhost:5000/message/date"

#### Parametros requeridos (en forma de diccionario)

'Collection': " "

'Type_Chat': " "

'Name_Chat': " "

'Date': '/18'( El año se escribe en el formato '/aa')

#### Ejemplo:

url = "http://localhost:5000/message/date"

dato = {'Type_Chat':'Grupo', 'Name_Chat':'recuvenza', 'Collection': 'chat', 'Date': '/18' }

frases = requests.get(url, data=dato)

Repuesta:

```
[{'Name_User': 'Carlos:',
  'Message': 'Thank you brother!',
  'Date': '12/21/18 15:15'},
 {'Name_User': 'Carlos:', 'Message': '', 'Date': '12/21/18 15:21'},
 {'Name_User': 'Carlos:', 'Message': '', 'Date': '12/23/18 16:46'},
 {'Name_User': 'Carlos:',
  'Message': '<Multimedia omitted>',
  'Date': '12/24/18 12:16'},
 {'Name_User': 'Carlos:', 'Message': '', 'Date': '12/27/18 15:36'},
 {'Name_User': 'Cristian:',
  'Message': "Good morning, thank you, I'll be waiting for the information, thanks for the support",
  'Date': '12/22/18 17:03'}]
```



### 6.- Solicitud de la polaridad media de cada usuario en un chat.

##### Endpoint = "http://localhost:5000/Polaridad"

#### Parametros requeridos (en forma de diccionario)

'Collection': " "

'Type_Chat': " "

'Name_Chat': " "

#### Ejemplo:

url = "http://localhost:5000/Polaridad"

dato = {'Type_Chat':'Grupo', 'Name_Chat':'recuvenza', 'Collection': 'chat'}

frases = requests.get(url, data=dato)

Repuesta:

```
[{'Name': 'Patricia:', 'mean': 0.0},
 {'Name': 'Edison:', 'mean': 0.121},
 {'Name': 'Sheldon:', 'mean': 0.131},
 {'Name': 'Latina:', 'mean': 0.168},
 {'Name': 'Pedro:', 'mean': 0.173},
 {'Name': 'Hermes:', 'mean': 0.194},
 {'Name': 'Cristian:', 'mean': 0.205}]

```


### 7.- Solicitud de la polaridad media de usuarios especificos en un chat.

##### Endpoint = "http://localhost:5000/Polaridad/User"

#### Parametros requeridos (en forma de diccionario)

'Collection': " "

'Type_Chat': " "

'Name_Chat': " "

'Name_User': [' ',' '] (los usurios se pasan en formato lista)

#### Ejemplo:

url = "http://localhost:5000/Polaridad/User"

dato = {'Type_Chat':'Grupo', 'Name_Chat':'recuvenza', 'Collection': 'chat', 'Names_user':['Patricia:', 'Lupita:', 'Yaritza:']}

frases = requests.get(url, data=dato)

Repuesta:

```
[{'Name': 'Patricia:', 'mean': 0.0},
 {'Name': 'Yaritza:', 'mean': 0.414},
 {'Name': 'Lupita:', 'mean': 0.733}]

```


### 8.- Solicitud de la Subjetividad media de todos los usuarios en un chat.

##### Endpoint = "http://localhost:5000/subjetividad"

#### Parametros requeridos (en forma de diccionario)

'Collection': " "

'Type_Chat': " "

'Name_Chat': " "

#### Ejemplo:

url = "http://localhost:5000/subjetividad"

dato = {'Type_Chat':'Grupo', 'Name_Chat':'recuvenza', 'Collection': 'chat'}

frases = requests.get(url, data=dato)

Repuesta:

```
[{'Name': 'Patricia:', 'mean': 0.0},
 {'Name': 'Sheldon:', 'mean': 0.186},
 {'Name': 'Carlos:', 'mean': 0.197},
 {'Name': 'Pedro:', 'mean': 0.206},
 {'Name': 'Hermes:', 'mean': 0.207},
 {'Name': 'Edison:', 'mean': 0.223}]

```

### 9.- Solicitud de la Subjetividad media de todos los usuarios en un chat.

##### Endpoint = "http://localhost:5000/subjetividad/User"

#### Parametros requeridos (en forma de diccionario)

'Collection': " "

'Type_Chat': " "

'Name_Chat': " "

'Name_User': [' ',' '] (los usurios se pasan en formato lista)


#### Ejemplo:

url = "http://localhost:5000/subjetividad/User"

dato = {'Type_Chat':'Grupo', 'Name_Chat':'recuvenza', 'Collection': 'chat', 'Names_user':['Patricia:', 'Lupita:', 'Yaritza:']}

frases = requests.get(url, data=dato)

Repuesta:

```
[{'Name': 'Patricia:', 'mean': 0.0},
 {'Name': 'Yaritza:', 'mean': 0.364},
 {'Name': 'Lupita:', 'mean': 0.733}]

```

Existen otros dos endpoint que permiten obtener una grafica donde se plotea la polaridad de cada usuario y en dicho scatter se traza la polaridad media que tiene el chat y ademas se indica una zona de alerta en caso de que algun valor se encuentre en dicha zona. 

lo anterior se aplica de igual manera para la subjetividad

### 10.- Skatter plot de polaridad.

##### Endpoint = "http://localhost:5000/plot/<Collection>/<Type_Chat>/<Name_Chat>"

#### Parametros requeridos (directamente en el endpoint)

Collection

Type_Chat

Name_Chat

#### Ejemplo:

Repuesta:

### Imagen del endpoint

<img src=img/polaridad.jpg width="600"> 




### 11.- Skatter plot de subjetividad.

##### Endpoint = "http://localhost:5000/plot2/<Collection>/<Type_Chat>/<Name_Chat>"

#### Parametros requeridos (directamente en el endpoint)

Collection

Type_Chat

Name_Chat

#### Ejemplo:

Repuesta:

### imagen del archivo.txt

<img src=img/subjetividad.jpg width="1000"> 



## Metodo POST

En este medoto existen 2 endpoint, los cuales consisten en agregar informacion a la base de datos, sin embargo esta informacion se puede agregar uno a uno o a travez de un archivo .txt con un formato especifico.

#### Nota: Los dos endpoint verifican si el contenido que se intenta agregar ya existe, en caso de que haya la coincidencia el proceso pasa a la siguiente infomracion (caso para el .txt), pero si esta en el otro endpoint le aparecera el mensaje siguiente "No se puede agregar, ya en la base de datos existe una coincidencia para todos los datos".

### 1.- Agregar un usuario con su mensaje a la base de datos.

##### "http://localhost:5000/insertar"

#### Parametros requeridos (en forma de diccionario)

'Collection': " "

'Type_Chat': " "

'Name_Chat': " "

'Message' : " "

'Date': " "

#### Ejemplo

url = "http://localhost:5000/insertar"

dato = {'Type_Chat':'', 'Name_Chat':'Saleciano', 'Collection': 'prueba', 'Name_User':'Maria', 'Message':'hola',  'Date': '12/12/18'}

frases = requests.post(url, data=dato)

respuesta:
    si se agrega "Agregado exitosamente a la base de datos"
    si no se agrega "No se puede agregar, ya en la base de datos existe una coincidencia para todos los datos"


### 2.- Agregar un archivo .txt de una data de mensaje a la base de datos.

Se realiza directamente desde el explorador.

##### endpoint = "http://localhost:5000/load"

#### Pasos:

##### A) Ir a endpoint

##### B) Rellenar la informacion

##### C) Enviarla


##### NOTA: Para que la informacion se agregue adecuada mente el archivo .txt debe tener un formato donde cada mensaje debe ser una linea continua y esta misma debe estar compuesta de 3 segmentos (Fecha, Usuario, Mensaje).

Formato de cada linea 

Fecha ---- Debe tener el formato dd/mm/aa

luego un espacio, un guion y otro espacio.

Usuario: nombre del que envia el mensaje y dos puntos.

luego espacio

Mesaje ---- el contenido del mensaje



#### Se uso este formato ya que es el que tiene whatsapp cuando se exportan su chat a un archivo .txt 


### Imagen del endpoint

<img src=img/carga.jpg width="1000"> 



### imagen del archivo.txt

<img src=img/texto.jpg width="1000"> 


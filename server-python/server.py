
import pymysql
from flask import Flask, request
from flask import jsonify
import json
from flask_cors import CORS
from markupsafe import escape







# conectarse a la base de datos:
def obtener_conexion():
    return pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='1505',
                                db='domotica')
    

app = Flask(__name__)
CORS(app)
app.run(debug=True)



   


@app.route("/")
def index():
    return "Welcome to Sunday Intelligence"

#OBTENER TODOS LOS DISPOSITIVOS
def getDevices():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT * FROM lights')
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return jsonify(json_data)

@app.route("/devices")
def devices():
    d = getDevices()
    return d

#OBTENER LUCES

def getDevicesLights():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT * FROM lights WHERE category = "light"')
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return jsonify(json_data)

   
@app.route("/devices/lights")
def getLights():
    d = getDevicesLights()
   
    
    return d
   



#OBTENER AIRES ACONDICIONADO

def getDevicesAir():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT * FROM lights WHERE category = "air"')
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return jsonify(json_data)

   
@app.route("/devices/air")
def getAir():
    d = getDevicesAir()
    return d
   
#OBTENER TOMACORRIENTES

def getDevicesPlug():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT * FROM lights WHERE category = "plug"')
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return jsonify(json_data)

   
@app.route("/devices/plug")
def getPlug():
    d = getDevicesPlug()
    return d
   


# ACTUALIZAR ESTADO DISPOSITIVO
@app.route('/lights/data/<id>', methods=['PUT'])
def pepito(id):
    
    data = request.json
    estado = data.get('estado') 
    idDevice = f'{id}'
    
    print(estado)
    print(idDevice)
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE lights SET estado = %s WHERE id = %s", (estado,idDevice))
        conexion.commit()
    return data
   
def getDevicesroom(r):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM lights WHERE room = %s",(r))
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return jsonify(json_data)


   
@app.route('/rooms/<room>', methods=['GET'])
def getRooms(room):
    r = f'{room}'
    
    d = getDevicesroom(r)
    return d
  
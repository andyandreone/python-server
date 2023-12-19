
import pymysql
from flask import Flask
from flask import jsonify
import json







# conectarse a la base de datos:
def obtener_conexion():
    return pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='1505',
                                db='domotica')
    

app = Flask(__name__)


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
   



#-------------------------------

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
   



# router.get('/devices/lights', getDatosLights);

# router.get('/lights/count', getCountLights);

# router.get('/lights/data/:id',getDataLight)

# router.post('/light', saveDeviceLight);

# router.delete('/lights/data/:id', deleteDataLight)

# router.put('/lights/data/:id', updateDataLight)

# //CURTAINS

# router.get('/curtains/datos', getDatosCurtains);

# //AIR
# router.get('/devices/air', getDatosAir);


# //TOMACORRIENTE
# router.get('/devices/plug', getDatosPlug);

# //TOMACORRIENTE
# router.get('/devices/rooms/:room', getDatosRooms);

# /----------- CORTINAS ---------------------------------

# export const getDatosCurtains = async (req,res) => {
#    const connection = await connect()
#    const [rows] = await connection.query("SELECT * FROM device WHERE category = 'curtain'")
#    res.json(rows);
# }



# //----------- LUCES ---------------------------------

# export const getDatosLights = async (req,res) => {

#     const connection = await connect()
    
#     const [rows] =  await connection.query("SELECT * FROM lights WHERE category = 'light'")
    
#     res.json(rows);
#  }
 
# //----------- air ---------------------------------

# export const getDatosAir = async (req,res) => {

#     const connection = await connect()
    
#     const [rows] =  await connection.query("SELECT * FROM lights WHERE category = 'air'")
    
#     res.json(rows);
#  }


#  //----------- air ---------------------------------

# export const getDatosPlug = async (req,res) => {

#     const connection = await connect()
    
#     const [rows] =  await connection.query("SELECT * FROM lights WHERE category = 'plug'")
    
#     res.json(rows);
# }


#  //----------- rooms ---------------------------------

#  export const getDatosRooms= async (req,res) => {
#     const connection = await connect()
#     const [rows] = await connection.query('SELECT * FROM lights WHERE room = ?' , [req.params.room,])
    
#     if(rows.length>0){
#         res.json(rows)
#     }
#     else{
#         res.json('no se encontraron resultados')
#     }

# }
# //-----GENERALES----------
 
#  export const getDataLight = async (req,res) => {
#      const connection = await connect()
#      const [rows] = await connection.query('SELECT * FROM lights WHERE id = ?' , [req.params.id,])
     
#      if(rows.length>0){
#          res.json(rows[0])
#      }
#      else{
#          res.json('no se encontraron resultados')
#      }
#  }
 
#  export const getCountLights = async (req,res) => {
#      const connection = await connect();
#      const [rows] = await connection.query('SELECT COUNT (*) FROM device')
     
#      res.json(rows[0]["COUNT (*)"]);
#  }
 
#  export const saveDeviceLight = async (req,res) => {
#      const connection = await connect()
#      const [results] = await connection.query('INSERT INTO device (name, nameIcon) VALUES (?,?)', [req.body.name, req.body.nameIcon])
     
#      res.json({
#             id: results.insertId,
#          ...req.body,
#      });
#  }
 
#  export const deleteDataLight = async (req,res) => {
#      const connection = await connect()
#      await connection.query('DELETE FROM device WHERE id=?',[req.params.id])
#      res.sendStatus(204)
#  }
 
#  export const updateDataLight = async (req,res) => {
#      const connection = await connect()
#      await connection.query('UPDATE lights SET ? WHERE id = ?', [
#              req.body,
#              req.params.id
#          ])
         
#      res.sendStatus(204)
#  }
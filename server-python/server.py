# conectar a la base de datos
import pymysql
from flask import Flask
from flask import jsonify
import json




#--------------------------------------------


import psycopg2
from psycopg2 import sql
# def obtener_conexion():
conn = psycopg2.connect(host="janus-cluster.ci9p5pgbpkpv.us-west-2.redshift.amazonaws.com",
                        port=5439,
                        user="janusdb_produccion",
                        password="Prod1234",
                        database="lfdb_prod")







#---------------------------------------------
# def obtener_conexion():
#     return pymysql.connect(host='127.0.0.1',
#                                 user='root',
#                                 password='1505',
#                                 db='domotica')




#funciones
def getDatos():
    print('pepe2')
    # conn = obtener_conexion()
    select_query = sql.SQL("SELECT max(id) FROM teting_table;")
    cursor = conn.cursor()
    cursor.execute(select_query)
    rows = cursor.fetchall()
    tmp_id = float(rows[0][0])+1
    select_query = sql.SQL(f"INSERT INTO teting_table values ({tmp_id}, 1);commit")
   
    cursor = conn.cursor()
    # time.sleep(0.1)
    cursor.execute(select_query)
    return 'pepe'
    



# def getDatos():
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute('SELECT * FROM lights')
#         row_headers=[x[0] for x in cursor.description] #this will extract row headers
#         rv = cursor.fetchall()
#         json_data=[]
#         for result in rv:
#             json_data.append(dict(zip(row_headers,result)))
#         return jsonify(json_data)


# def getDatos():
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute('SELECT * FROM lights')
#         rows = cursor.fetchall()
#         result = []
#         for row in rows:
#             d={}
#         for i, col in enumerate(cursor.description):
#             d[col[0]]= row[i]
#             result.append(d)
#     json_result = json.dumps(result)
#     print(json_result)            
#     conexion.close()
#     return json_result




# # Execute the SQL query
# query = “SELECT * FROM table_name”
# cursor.execute(query)

# # Fetch all rows and convert to a list of dictionaries
# rows = cursor.fetchall()
# result = []
# for row in rows:
# d = {}
# for i, col in enumerate(cursor.description):
# d[col[0]] = row[i]
# result.append(d)

# # Convert the list of dictionaries to JSON and print it
# json_result = json.dumps(result)
# print(json_result)





# server



app = Flask(__name__)

# @app.route("")
# def index():
#     d = getDatos()
#     print(d)
#     return jsonify(d)

@app.route("/lights/datos")
def index():
    d = getDatos()
    return d
   



    

    

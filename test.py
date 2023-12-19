# # from flask import Flask
# # from datetime import datetime
# # from flask import render_template
# # from flask import redirect
# # application = Flask(__name__)

# # @application.route('/')
# # @application.route('/home')
# # def home():
# # 	return render_template(
# #         'MainPage.html'
# #     )

# # @application.route('/nasa')
# # def nasaMethod():
# # 	return redirect("http://www.seas.virginia.edu/pubs/spectra/pdfs/nasapartnerships.pdf", code=302)

# # @application.route('/resume')
# # def resumeMethod():
# # 	return redirect("https://s3.amazonaws.com/GautamResume/GautamKanumuruResume.pdf", code=302)

# # @application.route('/uvradiationabstract')
# # def uvabstract():
# # 	return redirect("https://s3.amazonaws.com/GautamResume/UVAbstract.pdf")

# # @application.route('/uvradiationpaper')
# # def uvpaper():
# # 	return redirect("https://s3.amazonaws.com/GautamResume/UVPaper.pdf")

# # @application.route('/fieabstract')
# # def fieabstract():
# # 	return redirect("https://s3.amazonaws.com/GautamResume/FIEAbstract.pdf")

# # @application.route('/fiepaper')
# # def fiepaper():
# # 	return redirect("https://s3.amazonaws.com/GautamResume/FIEPaper.pdf")
	
# # @application.route('/testing')
# # def testMethod():
# # 	return "Is this working"

# # @application.errorhandler(404)
# # def page_not_found(e):
# #     """Custom 404 Page."""
# #     return render_template('ErrorPage.html'), 404

# # @application.errorhandler(500)
# # def page_not_found(e):
# #     """Custom 500 Page."""
# #     return render_template('500Error.html'), 500

# # if __name__ == "__main__":
# #     application.run(host='0.0.0.0')










# # 	from bd import obtener_conexion


# # def insertar_juego(nombre, descripcion, precio):
# #     conexion = obtener_conexion()
# #     with conexion.cursor() as cursor:
# #         cursor.execute("INSERT INTO juegos(nombre, descripcion, precio) VALUES (%s, %s, %s)",
# #                        (nombre, descripcion, precio))
# #     conexion.commit()
# #     conexion.close()


# # def obtener_juegos():
# #     conexion = obtener_conexion()
# #     juegos = []
# #     with conexion.cursor() as cursor:
# #         cursor.execute("SELECT id, nombre, descripcion, precio FROM juegos")
# #         juegos = cursor.fetchall()
# #     conexion.close()
# #     return juegos


# # def eliminar_juego(id):
# #     conexion = obtener_conexion()
# #     with conexion.cursor() as cursor:
# #         cursor.execute("DELETE FROM juegos WHERE id = %s", (id,))
# #     conexion.commit()
# #     conexion.close()


# # def obtener_juego_por_id(id):
# #     conexion = obtener_conexion()
# #     juego = None
# #     with conexion.cursor() as cursor:
# #         cursor.execute(
# #             "SELECT id, nombre, descripcion, precio FROM juegos WHERE id = %s", (id,))
# #         juego = cursor.fetchone()
# #     conexion.close()
# #     return juego


# # def actualizar_juego(nombre, descripcion, precio, id):
# #     conexion = obtener_conexion()
# #     with conexion.cursor() as cursor:
# #         cursor.execute("UPDATE juegos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
# #                        (nombre, descripcion, precio, id))
# #     conexion.commit()
# #     conexion.close()









# [{"id":1,"name":"luz comedor 14","estado":1,"nameIcon":"lightbulb","category":"light"},{"id":2,"name":"luz comedor 4","estado":1,"nameIcon":"lightbulb","category":"light"},{"id":3,"name":"luz cocina 1","estado":0,"nameIcon":"lightbulb","category":"light"}]


# [
#   {
#     "estado": 1,
#     "id": 1,
#     "name": "luz comedor 6",
#     "nameIcon": "lightbulb"
#   },
#   {
#     "estado": 0,
#     "id": 2,
#     "name": "luz comedor 134",
#     "nameIcon": "lightbulb"
#   },
#   {
#     "estado": 1,
#     "id": 3,
#     "name": "luz comedor 2124",
#     "nameIcon": "lightbulb"
#   }
# ]




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
    


# consulta obtener datos
def getDatos():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT * FROM lights')
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return jsonify(json_data)


# #funciones
# def getDatos():
#     obtener_conexion()
#     # conn = obtener_conexion()
#     select_query = sql.SQL("SELECT max(id) FROM teting_table;")
#     cursor = conn.cursor()
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     tmp_id = float(rows[0][0])+1
#     select_query = sql.SQL(f"INSERT INTO teting_table values ({tmp_id}, 1);commit")
   
#     cursor = conn.cursor()
#     # time.sleep(0.1)
#     cursor.execute(select_query)
#     return 'pepe'
    





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
   



    

    
#  import psycopg2
# # from psycopg2 import sql
# # # def obtener_conexion():
# # conn = psycopg2.connect(host="janus-cluster.ci9p5pgbpkpv.us-west-2.redshift.amazonaws.com",
# #                         port=5439,
# #                         user="janusdb_produccion",
# #                         password="Prod1234",
# #                         database="lfdb_prod")

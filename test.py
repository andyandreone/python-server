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



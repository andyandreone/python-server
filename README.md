
COMANDOS:
 
 Posicionarte en la carpeta principal:

 `cd server-python`

 Crear entorno virtual:

 `python3 -m venv .venv`

 Activar entorno virtual:

 `. .venv/bin/activate`

 Instalar Flask:

 `pip install Flask`

 Ejecutar server:

 `flask --app server run`


 ROUTES:

obtener todos los dispositivos:

 GET `localhost:5000/devices`

obtener todos las luces:

 GET `localhost:5000/devices/lights`

obtener todos los aires acondicionado:

 GET `localhost:5000/devices/air`

 obtener todos los tomacorrientes:

 GET `localhost:5000/devices/plug`

 actualizar estado dispositivo:

 PUT `localhost:5000/devices/data/id`

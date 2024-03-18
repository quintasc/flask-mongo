# flask-mongo
Esta aplicación gestionará las tareas de usuario: logging in (conectarse), logging out (desconectarse) y sign up (registrarse)

## Instalación
Need to pip render_template, url_for, request, session, redirect, flash modules
Necesitarás instalar con pip los siguientes paquetes: flask, flask_pymongo y bcrypt (para encriptar la password) para usar las funciones:
### render_template (from flask): permite la integración de archivos HTML con datos dinámicos en Python
### url_for (from flask): sirve para que en lugar de escribir manualmente las URLs en tu código, se generen automáticamente a partir de la ruta
### request (from flask): en Flask es un objeto global de Python que representa la solicitud del cliente al servidor
### session (from flask): en Flask es un diccionario que se utiliza para almacenar información específica del usuario de manera persistente a lo largo de las solicitudes. La información en una sesión se almacena en el lado del cliente, generalmente en las cookies del navegador, y los datos están cifrados, lo que significa que son seguros y no pueden ser fácilmente leídos o alterados
### redirect (from flask): en Flask es una utilidad muy importante para controlar el flujo de una aplicación web, permitiendo redirigir al usuario a otra ruta o URL específica
### flash (from flask): es una herramienta poderosa utilizada para enviar mensajes temporales entre vistas.

### PyMongo (from flask_pymongo): controlador para poder crear conexiones y trabajar contra una BD MongoDB





Then add the mongodb details

app.config['MONGO_dbname'] = 'users'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users'
Usage
Once installed, Start the app with:

python app.py
We now have a basic working application that makes use of session-based authentication. To round things off, we should provide a callback for login failures:

Contributing
We welcome contributions! If you would like to hack on Flask-MongoDB-Login, please follow these steps:

Fork this repository
Make your changes
Install the requirements
Submit a pull request after running make check (ensure it does not error!)
Please give us adequate time to review your submission. Thanks!

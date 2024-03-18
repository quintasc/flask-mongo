# flask-mongo
Esta aplicación gestionará las tareas de usuario: logging in (conectarse), logging out (desconectarse) y sign up (registrarse)

## Base de Datos
Los datos se almacenarán en una BD MongoDB, en una colección llamada 'users'

## Instalación
Need to pip render_template, url_for, request, session, redirect, flash modules
Necesitarás instalar con pip los siguientes paquetes: flask, flask_pymongo y bcrypt (para encriptar la password) para usar las funciones:
### render_template (from flask): 
permite la integración de archivos HTML con datos dinámicos en Python
### url_for (from flask): 
sirve para que en lugar de escribir manualmente las URLs en tu código, se generen automáticamente a partir de la ruta
### request (from flask): 
en Flask es un objeto global de Python que representa la solicitud del cliente al servidor
### session (from flask): 
en Flask es un diccionario que se utiliza para almacenar información específica del usuario de manera persistente a lo largo de las solicitudes. La información en una sesión se almacena en el lado del cliente, generalmente en las cookies del navegador, y los datos están cifrados, lo que significa que son seguros y no pueden ser fácilmente leídos o alterados
### redirect (from flask): 
en Flask es una utilidad muy importante para controlar el flujo de una aplicación web, permitiendo redirigir al usuario a otra ruta o URL específica
### flash (from flask): 
es una herramienta poderosa utilizada para enviar mensajes temporales entre vistas.

### PyMongo (from flask_pymongo): 
controlador para poder crear conexiones y trabajar contra una BD MongoDB

## Instrucciones
Investiga y básate en las prácticas: 
- TC: Creating Web Applications with Flask para crear el proyecto Flask
- TC: Conectar a una BD MongoDB Atlas
Además cuentas en este repositorio con el esqueleto del proyecto y el código relativo a los html y css necesarios

## Rúbrica
- Login funcional (funciona el formulario, comprueba si el usuario está registrado y aparece mensaje de usuario/password incorrectos o redirige a index.html) -- 25%
- Sign Up funcional (funcional el formulario, redirige a index.html y aparece mensaje de logged in. Se debe dar de alta un nuevo documento en la colección) -- 25%
- Crear una nueva opción que permita modificar la password de un usuario -- 25%
- Modifica el funcionamiento del botón logout para que elimine de la base de datos al usuario conectado (este comportamiento no es el habitual y obedece úncamente a cuestiones académicas) -- 25%




Pasos

1.) crear entorno virtual con python -m venv venv

2.) activar entorno virtual con ./venv/scripts/activate

3.) pip install fastapi

4.) pip install jinja2

5.) pip install werkzeug

6.) debe tener instalado sqlite3

7.) activar el servidor de uvicorn con uvicorn main:app --reload

4.) en el navegador localhost:8000


main.py:

Descripción
Este código implementa una API usando FastAPI para operaciones CRUD básicas en una base de datos de usuarios. Utiliza formularios HTML para recibir datos del usuario.

Endpoints:
GET "/":

Método: GET
Descripción: Renderiza la página de inicio.
POST "/":

Método: POST
Descripción: Renderiza la página de inicio (utilizado para redireccionar).
GET "/register":

Método: GET
Descripción: Renderiza la página de registro.
GET "/user":

Método: GET
Descripción: Redirecciona a la página de inicio ("/").
POST "/user":

Método: POST
Descripción: Verifica el usuario y la contraseña proporcionados. Renderiza la página del usuario si la verificación es exitosa, de lo contrario redirecciona a la página de inicio ("/").
POST "/create_user":

Método: POST
Descripción: Crea un nuevo usuario con los datos proporcionados en el formulario.
POST "/delete_user":

Método: POST
Descripción: Elimina un usuario basado en el ID proporcionado y verifica la contraseña antes de eliminarlo.
POST "/update_password":

Método: POST
Descripción: Actualiza la contraseña de un usuario basado en el ID proporcionado y verifica la contraseña actual antes de realizar el cambio.

Funcionalidad:

El código utiliza plantillas Jinja2 para renderizar las páginas HTML correspondientes.
Las operaciones CRUD se realizan utilizando métodos HTTP GET y POST en diferentes rutas.
Se manejan acciones como crear usuario, eliminar usuario, actualizar contraseña y verificar credenciales.

Estructura:
El código utiliza una estructura modular, importando funciones específicas desde otros archivos para realizar verificaciones de usuario, manipulación de la base de datos y otras tareas.
Consideraciones de seguridad:
Se realizan comprobaciones de contraseña antes de ejecutar acciones como eliminar usuario o actualizar contraseña.
--------------------------------------------------------------------------------------------------------------------
handle_db.py:

Clase HandleDB

Métodos:
Constructor __init__:

Descripción: Inicializa la conexión a la base de datos SQLite.
Funcionalidad: Establece la conexión y el cursor para la base de datos SQLite ubicada en "./users.sqlite".
get_all:

Descripción: Obtiene todos los usuarios de la tabla "users".
Funcionalidad: Ejecuta una consulta SQL para seleccionar todos los registros de la tabla "users" y devuelve una lista con los datos de todos los usuarios.
get_only:

Descripción: Obtiene un usuario específico por su nombre de usuario.
Funcionalidad: Ejecuta una consulta SQL para seleccionar un registro de la tabla "users" donde el nombre de usuario coincide con el proporcionado y devuelve los datos de ese usuario.
get_only_id:

Descripción: Obtiene un usuario por su ID.
Funcionalidad: Ejecuta una consulta SQL para seleccionar un registro de la tabla "users" donde el ID coincide con el proporcionado y devuelve los datos de ese usuario.
insert:

Descripción: Inserta un nuevo usuario en la tabla "users".
Funcionalidad: Ejecuta una consulta SQL para insertar un nuevo registro en la tabla "users" con los datos proporcionados en el diccionario data_user.
delete_user_by_id:

Descripción: Elimina un usuario basado en su ID.
Funcionalidad: Ejecuta una consulta SQL para eliminar un registro de la tabla "users" donde el ID coincide con el proporcionado.
update_password_for_user:

Descripción: Actualiza la contraseña de un usuario por su ID.
Funcionalidad: Encripta la nueva contraseña utilizando el algoritmo "pbkdf2:sha256:30" de Werkzeug y luego ejecuta una consulta SQL para actualizar la contraseña del usuario cuyo ID coincide con el proporcionado.
Destructor __del__:

Descripción: Cierra la conexión a la base de datos.

Funcionalidad: Cierra la conexión a la base de datos SQLite cuando el objeto HandleDB es destruido.

Consideraciones:
Se utilizan consultas SQL directas, lo que puede representar riesgos de seguridad como la inyección de SQL si los datos no son validados correctamente antes de ejecutar las consultas.
La contraseña se almacena en la base de datos después de ser encriptada usando el método generate_password_hash de Werkzeug para aumentar la seguridad.
La clase maneja operaciones básicas de CRUD (Create, Read, Update, Delete) relacionadas con la tabla "users" en la base de datos SQLite.
------------------------------------------------------------------------------------------------------------------------------------
user.py:

Clase User

Atributos:
data_user (diccionario): Almacena los datos del usuario.

Métodos:
Constructor __init__:

Descripción: Inicializa un objeto User con datos de usuario.

Parámetros: data_user (dict) - Datos del usuario a ser almacenados y manipulados.

Funcionalidad:
Crea una instancia de HandleDB para interactuar con la base de datos.
Almacena los datos del usuario proporcionados en el atributo data_user.
create_user:

Descripción: Crea un nuevo usuario.

Funcionalidad:
Asigna un ID único al usuario utilizando el método _add_id.
Encripta la contraseña del usuario utilizando el método _pass_encrypt.
Inserta los datos del usuario en la base de datos utilizando el método insert de HandleDB.
_add_id:

Descripción: Asigna un ID único al usuario.

Funcionalidad:
Obtiene todos los usuarios existentes utilizando get_all de HandleDB.
Si no hay usuarios, asigna el ID "1" al nuevo usuario. De lo contrario, asigna un ID incrementado basado en el último ID de usuario existente.
_pass_encrypt:

Descripción: Encripta la contraseña del usuario.

Funcionalidad:
Utiliza generate_password_hash de Werkzeug para encriptar la contraseña del usuario utilizando el algoritmo "pbkdf2:sha256:30".

Consideraciones:
La clase User se utiliza para manejar la creación de usuarios en la base de datos.
Se utiliza un objeto HandleDB para interactuar con la base de datos, realizando operaciones de inserción de datos.
Genera un ID único para cada nuevo usuario y encripta la contraseña antes de insertarla en la base de datos para mejorar la seguridad.
La lógica para asignar un ID único podría tener problemas si hay múltiples usuarios accediendo a la aplicación simultáneamente, ya que podría generar IDs duplicados.
------------------------------------------------------------------------------------------------------------------------------------------------------------
check_password.py:

Funciones:
check_user(username, password):

Descripción: Verifica las credenciales del usuario durante el inicio de sesión.

Parámetros:
username (str): Nombre de usuario ingresado durante el inicio de sesión.
password (str): Contraseña ingresada durante el inicio de sesión.

Funcionalidad:
Crea una instancia de HandleDB.
Obtiene los datos del usuario mediante get_only de HandleDB usando el username proporcionado.
Comprueba si el usuario existe y si la contraseña coincide utilizando check_password_hash de Werkzeug para comparar la contraseña ingresada con la contraseña almacenada en la base de datos.
Si las credenciales son válidas, devuelve los datos del usuario. De lo contrario, devuelve None.
check_user_id(user_id, password):

Descripción: Verifica las credenciales del usuario durante las operaciones de eliminación y actualización.

Parámetros:
user_id (str): ID del usuario sobre el cual se realizará la acción de eliminación o actualización.
password (str): Contraseña ingresada durante la operación.

Funcionalidad:
Crea una instancia de HandleDB.
Obtiene los datos del usuario mediante get_only_id de HandleDB usando el user_id proporcionado.
Comprueba si el usuario existe y si la contraseña coincide utilizando check_password_hash de Werkzeug para comparar la contraseña ingresada con la contraseña almacenada en la base de datos.
Si las credenciales son válidas, devuelve los datos del usuario. De lo contrario, devuelve None.

Consideraciones:
Estas funciones son utilizadas para verificar las credenciales del usuario durante diferentes operaciones como inicio de sesión, eliminación o actualización.
Utilizan el objeto HandleDB para acceder a la base de datos y comparan las contraseñas encriptadas con check_password_hash para garantizar la autenticidad del usuario antes de permitir operaciones críticas.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Plantillas jinja2 de html para una gestion de ventanas dinámica.

# BibliotecaComunitaria [![Build Status](https://travis-ci.org/dantebarba/BibliotecaComunitaria.svg?branch=master)](https://travis-ci.org/dantebarba/BibliotecaComunitaria)
Biblioteca comunitaria. Proyecto correspondiente a TPOO 2017.

# Instalacion del proyecto

## Requisitos


- API Facebook:
  Antes de comenzar con el tutorial de instalación cabe aclarar que deberán crear una aplicación de Facebook que
  permita el login de los usuarios.

  Para hacerlo tiene que realizar los siguiente:

  1. Loguearse normalmente en Facebook e ingresar en la siguiente url: https://developers.facebook.com/apps/
  2. Ingresar en “Mis aplicaciones” → “Agregar aplicación”.
  3. Luego seleccionar como tipo de aplicación “Inicio de sesión con Facebook” → “www”(web)
  4. Como URL del sitio web colocar: http://localhost:8080/hello
  5. Luego de crear la aplicación, en el panel de administración busque el ID de la aplicación creada. Algo como
  esto: 848529051971750
  6. En la clase del proyecto de pharo CommunityLibrary en el initialize deberá reemplazar los valores:
  7. newClientID por el ID de su aplicación y SecretID por la clave secreta de su aplicación.
  8. Nota: Sólo el creador de la aplicación podrá loguearse ya que es para pruebas de desarrollo.
  Para loguear otros usuarios deberá darles permiso desde el panel de administración en la opción “roles”.

- Mongo DB

  Descargar e instalar la útima versión correspondiente a la arquitectura de su pc de MongoDB de la página o
  cial.

  https://www.mongodb.com/download-center#community
  B)Crear la siguiente carpeta: C:\data\db de no existir “data”, también crearla.
  C)Descargar e instalar el un gestor de base de datos para mongodb como lo es el gestor “robombongo” (ya que va a
  facilitar el manejo de la base de datos durante las pruebas) de su página o
  cial:

  https://robomongo.org/download

- Repositorios de Pharo.

  Sobre una imagen nueva de Pharo 4.0 hacer lo siguiente:
  Click izquierdo → Tools → Con

  guration Browser y realizar las instalaciones en dicho orden:

  1) Instalar la versión estable de Voyage mongo (EstebanLorenzano.47).
**ES IMPORTANTE INSTALAR PRIMERO VOYAGE MONGO ANTES DE MONGO TALK.**
  2) Instalar la version estable de Mongotalk (EstebanLorenzano.43)
  3) Instalar la versión estable de Seaside3 (topa.278)
  E)Agregar el repositorio de la cátedra en Monticello.
  Click izquierdo →Monticello Browser → +Repository (Seleccionar HTTP).
  Y pegar este contenido:

```
  MCHttpRepository
    location: 'https://catedras.lifia.info.unlp.edu.ar/monticello'
    user: 'tpoo2012'
    password: 'tpoo2012'
```

  Una vez hecho esto podrás acceder a el repositorio del proyecto en la ventana de diálogo que se abre.
  F)Buscar a la izquiera en los paquetes “CommunityLibraryFacebook”, clickearlo y a la derecha seleccionar la versión
  39 (CommunityLibraryFacebook-fmendiburu.39.mcz) y clickear “load”. Esto descargará sobre la imagen, la
  última versión del proyecto.


- Configuracion de base de datos:

  Se deberá crear la base de datos siguiento estos pasos:
  Click derecho sobre la conexión → Create database y ponerle de nombre **“comunidad”**.

  Click izquierdo → Tools → Seaside Control Panel → Click derecho sobre el espacio blanco → Add adaptor →
  seleccionar **“ZnZincServerAdapter** y click en “ok”. Quedará en el puerto 8080.
  Seleccionar el adaptor creado y click en "start".

>  Ejecutar el siguiente código en un “playground”.
>
>  `DBRepository conectar.`
>
>  Verificar que en el mongod que aceptó la conexión.
>  Luego ejecutar en el playground el siguiente código:
>  `(WAAdmin register: LoginComponent asApplicationAt: 'hello')preferenceAt: #sessionClass put: Sesion.`


**Estos pasos pueden ser reemplazados por el siguiente comando unificado**

`CommunityLibrary start.`

  Ir al navegador, entrar en: localhost:8080/hello y loguearse con Facebook

- Mocking

  Si en vez de utilizar base de datos, deseamos simplemente inicializar los servicios, con datos
  precargados en memoria, podemos ejecutar el siguiente comando:

  `CommunityLibrary mock.`

- Docker

  El proyecto se encuentra parcialmente dockerizado. Para utilizar las funcionalidades de telegram, se debe Ejecutar una micro aplicación montada sobre un contenedor de docker.

  Requisitos:
    - docker
    - docker-compose 3.1 o superior.

  Sobre la carpeta donde se ecuentra el archivo **docker-compose.yml**

```
  $ docker-compose build
  $ docker-compose up
```

  -----

  ## Configuración de Telegram

  La aplicación permite consultar reservas utilizando la app de mensajería Telegram. Esto se logra a través de los llamados
  **bots**. Los bots son aplicaciones con inteligencia automatizada que permiten la interacción entre usuarios. Estas aplicaciones son configurables a gusto del programador o quien las utilice.
    Para poder interactuar con un bot, primero es necesario crear uno. Para la aplicación **Biblioteca Comunitaria** se ha preconfigurado un bot llamado [**@BibliotecaComunitariaBot**](https://t.me/BibliotecaComunitariaBot) que puede ser buscado en la aplicación de Telegram de la plataforma que se desee utilizar.

#### Requisitos:

- Tener la microaplicacion "telegram_webserver" en
    ejecución
- Tener Pharo configurado con el servidor funcionando (probar ingresar a localhost:8080/hello)
- Tener una cuenta activa en Telegram.

#### Configuracion:

Ejecutar los siguientes comandos en **playground**
```
Gofer new
  squeaksource: 'Seaside30Addons';
  package: 'Seaside-REST-Core';
  package: 'Seaside-Pharo-REST-Core';
  package: 'Seaside-Tests-REST-Core';
  load.
```

#### Comandos disponibles:

- **/start** &rarr; Comando de entrada al bot.
- **/isbn {isbn}** &rarr; Muestra el libro con ISBN {isbn} si existe
- **/books** &rarr; Lista todos los libros disponibles en la biblioteca
- **/help** &rarr; Muestra la lista de comandos

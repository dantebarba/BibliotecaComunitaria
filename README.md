# BibliotecaComunitaria
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

  1) Instalar la version estable de Mongotalk (EstebanLorenzano.43)
  2) Instalar la versión estable de Voyage mongo (EstebanLorenzano.47)
  3) Instalar la versión estable de Seaside3 (topa.278)
  E)Agregar el repositorio de la cátedra en Monticello.
  Click izquierdo →Monticello Browser → +Repository (Seleccionar HTTP).
  Y pegar este contenido:

  ```
  MCHttpRepository
  location: 'https://catedras.lifia.info.unlp.edu.ar/monticello'
  user: 'tpoo2012'
  password: 'tpoo2012'`

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
  Ejecutar el siguiente código en un “playground”. 
  
  `DBRepository conectar.`

  Verificar que en el mongod que aceptó la conexión.
  Luego ejecutar en el playground el siguiente código:
  `(WAAdmin register: LoginComponent asApplicationAt: 'hello')preferenceAt: #sessionClass put: Sesion.`
  
  Ir al navegador, entrar en: localhost:8080/hello y loguearse con Facebook

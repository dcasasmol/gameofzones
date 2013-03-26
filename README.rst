=============
Game of Zones
=============

Game of Zones es una aplicación que utiliza información de una red social basada en la geolocalización para crear un escenario "real" en el que podemos conquistar territorios haciendo check-in's en ellos.

Objetivos
=========

* El uso de foursquare para almacenar datos sobre la actividad de los usuarios.
* El uso de Google Maps para representar estos datos.
* La busqueda de un sistema de puntuación que estimule y provoque al usuario a usar la aplicación con asiduidad.

Directorios
===========

    //manage.py (archivo par controlar el proyecto)
    //gameofzones/
    /__init__.py (archivo necesario para Python)
    /wsgi.py (archivo para desplegar el proyecto en el servidor)
    /settings.py (opciones del proyecto)
    /urls.py (dispensador de urls)
    //foursquare/
    /__init__.py (archivo necesario para Python)
    /admin.py (controlador de los modelos en la vista de admin)
    /models.py (modelos para la base de datos)
    /test.py (archivo para tests)
    /views.py (vistas de la aplicación)
    /migrations (directorio para South(migraciones))


Requisitos
==========

Game of Zones no es necesario ningún requisito. Sólo se necesita un navegador web y conexión a internet. También es necesario tener una cuenta en la web::

     https://www.foursquare.com

Instalación
===========

Sólo será necesario abrir en el navegador la dirección web (url) de la aplicación web.

Para obtener el código fuente se puede visitar el repositorio en GitHub del proyecto::

     https://github.com/axte/gameofzones

Documentación
=============

Próximamente...

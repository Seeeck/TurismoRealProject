# Proyecto: Turismo Real
> Un sistema de información web, en el cual, pueda permitir facilitar la ejecución  de los procesos involucrados y así ayudar a gestionar de mejor manera la información generada por la Agencias de Turismo Real

Desarrollado por:
- Franco Zambelli
- Juan Pablo Polanco
- Celso Villagra 
- Kevin Peréz

Carrera: Ingeniería en informática

## Requisitos del sistema
### Requisitos Generales
- Python 3.9.6
- Oracle Database XE 18.4
- SQL Developer 21.2.1.204.1703 
### Librerías utilizadas
- asgiref 3.4.1
- cx-Oracle 8.2.1
- Django 3.2.7
- django-betterforms 1.2
- Pillow 8.3.2
- pytz 2021.1
- six 1.16.0
- sqlparse 0.4.1
- Unipath 1.1
- rut_chile 2.0.1
- django-3-jet 1.0.8
- google-api-python-client 1.4.1

## Como ejecutar el proyecto
1. En consola crear un entorno
    ````powershell
    python -m venv EntornoTest
    ````
2. Iniciar entorno
    ````powershell
    EntornoTest\Scripts\activate
    ````
3. Instalar librebrias del proyecto
    ````powershell
    pip install -r requirements/requirements.txt
    ````
4. Pedir el documento __secret.json__.
5. Pegar __secret.json__ en: ``/turismorealproyect/turismorealproject/``

6. En Oracle SQL:
    1. En __SYS__ crea un nuevo usuario ejecutando los siguientes comandos de SQL
        ````sql
        alter session set "_Oracle_SCRIPT"=true;  
        create user admin_turismo identified by "1234";

        grant connect,resource to admin_turismo;

        alter user admin_turismo default tablespace users quota unlimited on users;
        ````
    2. Crea una nueva conexión llamada __BD_TURISMO_REAL__, con _admin_turismo_ como usuario administrador y valores por defecto. 

7. En consola y dentro del entorno migrar las tablas de Django a la Base de datos.
    ````powershell
    python manage.py migrate
    ````
8. Crea a un super usuario.
     ````powershell
     python manage.py createsuperuser
    ````
9. Ejecute los siguentes comandos de migración  
    ````powershell
    python manage.py migrate jet
    ````
    ````powershell
    python manage.py collectstatic
    ````
    ````powershell
    python manage.py migrate dashboard
    ````
    ````powershell
    python manage.py migrate dashboard
    ````
10. Arranca el proyecto
    ````powershell
    python manage.py runserver
    ````
11. Accede desde tu navegador:
    - Pagina de inicio:     
    http://127.0.0.1:8000/
    - Pagina administrador de la pagina:    
     http://127.0.0.1:8000/admin 

12. Para ingresar datos de prueba ejecute:
    ````powershell
    python manage.py loaddata generateReserva1.json
    ````
 
# Proyecto: Turismo Real
Desarrollado por:
- Franco Zambelli ( @Seeeck )
- Kevin Peréz ( )
Pruebas por:
- Celso Villagra 
- Juan Pablo Polanco ( @bluu124 )


## Como ejecutar
1. Iniciar entorno
````bash
pip install -r requirements/requirements.txt
````
2. Pedir secret.json al creador del proyecto.
3. Pegar secret.json en Turismorealproyect/turismorealproject/
4. Abrir proyecto
5. Ejecutar a la altura de TurismoRealProject/turismoRealProject
````bash
python manage.py makemigrations
````
6. Ejecutar para migrar la base de datos:
````bash
python manage.py migrate"
````
7. Ejecutar para iniciar proyecto: 
````bash
python manage.py runserver
````
9. En Oracle SQL:
````sql
alter session set "_Oracle_SCRIPT"=true;  
create user admin_turismo identified by "1234";

grant connect,resource to admin_turismo;

alter user admin_turismo default tablespace users quota unlimited on users;
````

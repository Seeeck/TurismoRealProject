1. Clonar proyecto

2. Iniciar entorno

````bash
   pip install -r 		requirements/requirements.txt
````
3. Pedir secret.json al creador del proyecto.
4. Pegar secret.json en turismorealproyect/turismorealproject/
5. iniciar proyecto
6. En Oracle SQL

````sql

alter session set "_Oracle_SCRIPT"=true;  
create user admin_turismo identified by "1234";

grant connect,resource to admin_turismo;

alter user admin_turismo default tablespace users quota unlimited on users;
````
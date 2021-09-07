1.Clonar proyecto
2.Iniciar entorno
3.pip install -r requirements/requirements.txt
4.pedir secret.json al creador del proyecto
5.pegar secret.json en turismorealproyect/turismorealproject/
6.iniciar proyecto


"""""""""""""""ORACLE DB"""""""""""""""""
alter session set "_Oracle_SCRIPT"=true;  
create user admin_turismo identified by "1234";

grant connect,resource to admin_turismo;

alter user admin_turismo default tablespace users quota unlimited on users;
""""""""""""""

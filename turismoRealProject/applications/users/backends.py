from django.contrib.auth.backends import ModelBackend
from .models import User
from django.db.models import Q



class EmailAuthBackend(ModelBackend):
    """
    Email Authentication Backend    Permite a un usuario acceder utilizando su correo electrónico y
    contraseña. Si la autenticación falla, lo intenta con el par
    usuario/contraseña.
    """


    def authenticate(
            self, request, username=None, password=None, **kwargs):
        """
        Autentica un usuario utilizando el correo electrónico
        como nombre de usuario.
        """
        
     
        try:
            print('######desde backends de User')
            user = User.objects.get(email=username)
            print(user)
            print('#######################')
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None


    def get_user(self, user_id):
        """Devuelve un objeto User a partir del user_id."""
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
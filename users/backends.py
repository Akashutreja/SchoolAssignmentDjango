from .models import User
from django.contrib.auth.backends import ModelBackend

#need to authenticate with email
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = User
        try:
            if username:
                email = username
            else:
                email = request.data.get('email')
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            print(user,user.check_password(password))
            if user.check_password(password):
                return user
        return None
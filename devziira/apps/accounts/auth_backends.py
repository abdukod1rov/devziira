from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model();


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(
            self, request, username=..., password=..., **kwargs
    ):
        try:
            if '@' in username:
                user = User.objects.get(username=username)
            else:
                user = User.objects.get(email=username)

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

        except User.MultipleObjectsReturned:
            return None

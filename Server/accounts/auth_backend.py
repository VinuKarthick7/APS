from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class UIDAuthBackend(ModelBackend):
    def authenticate(self, request, uid=None, password=None, **kwargs):
        if uid is None or password is None:
            return None

        try:
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None

from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from fake_user.models import FakeUser, FakeUserProxy

class FakeUserAuthBackend(object):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name, and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, username=None, password=None):
        # raise Exception(FakeUser.objects.get(email=username))
        try:
            fakeuser = FakeUserProxy.objects.get(email=username)
            pwd_valid = check_password(password, fakeuser.password)
            if pwd_valid:
                return fakeuser
        except FakeUserProxy.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return FakeUserProxy.objects.get(pk=user_id)
        except FakeUserProxy.DoesNotExist:
            return None
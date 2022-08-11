from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)

class FakeUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField('password', max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super().save(*args, **kwargs)



class PermissionsMixin():
    def has_perm(self, perm, obj=None):
        return False 

    def has_perms(self, perm, obj=None):
        return False 

    def has_module_perms(self, app_label):
        return False

    class Meta:
        abstract = True

class FakeUserProxy(FakeUser, PermissionsMixin):
    is_active = True
    is_staff = False 
    is_superuser = False 

    def is_anonymous(self):
        """
        Always returns False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    class Meta:
        proxy = True

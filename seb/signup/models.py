from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager, PermissionsMixin
# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')


        email = self.normalize_email(email)
        # print(new_user)

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserSignUp(AbstractUser,PermissionsMixin):

    options = (('male','Male'),('female','Female'),('non-binary','Non-binary'))
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField( max_length=254, unique=True)
    gender = models.CharField(choices=options, max_length=10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name","username"]
    objects = CustomAccountManager()

    def __str__(self):
        return self.username

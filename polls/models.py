from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser)


class Recipe(models.Model):
    creater = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    process = models.CharField(max_length=200)
    image = models.ImageField(width_field=None, height_field=None)
    date = models.DateField("prepared date")

    class MyUserManager(BaseUserManager):
        def create_user(self, email, date_of_birth, password=None):
            """
            Creates and saves a User with the given email, date of
            birth and password.
            """
            if not email:
                raise ValueError('Users must have an email address')

            user = self.model(
                email=self.normalize_email(email),
                date_of_birth=date_of_birth,
            )

            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_superuser(self, email, date_of_birth, password):
            """
            Creates and saves a superuser with the given email, date of
            birth and password.
            """
            user = self.create_user(
                email,
                password=password,
                date_of_birth=date_of_birth,
            )
            user.is_admin = True
            user.save(using=self._db)
            return user

    def __str__(self):
        return self.name


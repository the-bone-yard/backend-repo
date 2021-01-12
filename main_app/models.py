from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
class Park(models.Model):
    """Makes park instance for favorited park"""
    name = models.CharField(max_length=300)
    formatted_address = models.CharField(max_length=300)
    opening_hours = models.CharField(max_length=1000, default='')
    photo = models.CharField
    rating = models.CharField
    

def create_park(self, name, formatted_address, opening_hours, photo, rating, **extra_fields):
    park = self.model(name=self.name, formatted_address=self.formatted_address, opening_hours=self.opening_hours, photo=self.photo, rating=self.rating)
    park.save(using=self._db)

    return park
class UserManager(BaseUserManager):

    def create_user(self, email, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.save(using=self._db)

        return user

    def create_superuser(self, email):
        """Creates and saves new superuser"""
        user = self.create_user(email)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


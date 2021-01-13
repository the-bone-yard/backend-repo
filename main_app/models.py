from django.db import models
import code
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
class Park(models.Model):
    """Makes park instance for favorited park"""
    name = models.CharField(max_length=300)
    formatted_address = models.CharField(max_length=300)
    opening_hours = models.CharField(max_length=1000, default='')
    photo = models.CharField(max_length=1000, default='')
    rating = models.CharField(max_length=100, default='0')
    email = models.CharField(max_length=100, default='NO EMAIL')
    lat = models.FloatField(max_length=20, default=0.0)
    lng = models.FloatField(max_length=20, default=0.0)


def create_park(self, name, formatted_address, opening_hours, photo, rating, **extra_fields):
    code.interact(local=dict(globals(), **locals()))
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

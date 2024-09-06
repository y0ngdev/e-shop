from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import uuid
import json


class UserManager(BaseUserManager):
    def create_user(self, email, name, username, password=None):
        """
         Creates and saves a User with the given email, name, tc and password.
         """
        if not email:
            raise ValueError('User must have an email address')
        if not name:
            raise ValueError('User must have an Name')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, username, password=None):
        """
         Creates and saves a superuser with the given email, name, tc and password.
         """
        user = self.create_user(
            email,
            password=password,
            name=name,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=16)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    rating = models.JSONField(default=dict)

    def set_rating(self, rate, count):
        self.rating = json.dumps({
            'rate': float(rate),
            'count': int(count)
        })

    def get_rating(self):
        return json.loads(self.rating)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

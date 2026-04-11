from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, password = None):
        if not email:
            raise ValueError("Users must have an email address ")
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    # full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # staff user, non superuser
    admin = models.BooleanField(default=False) # superuser

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    
    object = UserManager()

    def __str__(self):
        return self.email
    
    
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
    

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name   

from django.db import models
from django.contrib.auth.models import (
    AbstractUser, BaseUserManager
)


class customUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.username


# class UserManager(BaseUserManager):
#     def create_user(self, email, password = None, is_active = True, is_staff = False, is_admin = False):
#         if not email:
#             raise ValueError("Users must have an email address ")
#         if not password:
#             raise ValueError("Users must have a password ")
#         user = self.model(
#             email = self.normalize_email(email)
#         )
#         user.set_password(password)
#         user.staff = is_staff
#         user.admin = is_admin
#         user.active = is_active
#         user.save(using=self._db)
#         return user
    
#     def create_staffuser(self, email, password=None):
#         user = self.create_user(
#             email, 
#             password=password,
#             is_staff= True
#         )
#         return user
#     def create_superuser(self, email, password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             is_staff=True,
#             is_admin=True
#         )
#         return True
    
    



# # Create your models here.

# class Customuser(AbstractBaseUser):
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)  # staff user, non superuser
#     admin = models.BooleanField(default=False) # superuser

#     USERNAME_FIELD = 'email'

#     REQUIRED_FIELDS = []
    
#     object = UserManager()

#     def __str__(self):
#         return self.email
    
    
#     def get_full_name(self):
#         return self.email

#     def get_short_name(self):
#         return self.email
    
#     def has_perm(self, perm, obj=None):
#         return True
    
#     def has_module_perms(self, app_label):
#         return True
    
#     @property
#     def is_staff(self):
#         return self.staff

#     @property
#     def is_admin(self):
#         return self.admin
    
#     @property
#     def is_active(self):
#         return self.active
    

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name   
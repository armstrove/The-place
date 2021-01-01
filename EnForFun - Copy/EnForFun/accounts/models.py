from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser, BaseUserManager
        )

class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self,email,full_name=None,password=None):
        user_obj = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True
        )
        return user_obj
    
    def create_superuser(self,email, full_name=None, password=None):
        user_obj = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user_obj

class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    active      = models.BooleanField(default=True) # can login 
    staff       = models.BooleanField(default=False) # staff user non superuser
    admin       = models.BooleanField(default=False) # superuser
    timestamp   = models.DateTimeField(auto_now_add=True)
    # confirm    = models.BooleanField(default=False)
    # confirmed_data    = models.DateTimeField(default=False)
    
    objects     = UserManager()
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email
        
    def get_short_name(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
        
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.admin
    
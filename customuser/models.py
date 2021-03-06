# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, first_name, last_name, password=None):
        
        if not email:
            raise ValueError('Users must have an email address')    
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )
        
        if password is None:
            password = self.make_random_password()    
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)    
        user.is_admin = True
        user.save(using=self._db)
        return user
        

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True,
    )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'last_name']
    
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
        
    def get_first_name(self):
        return self.first_name
        
    def get_last_name(self):
        return self.last_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
    
    
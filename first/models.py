# coding: utf-8
from __future__ import unicode_literals

 
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class SUserManager(BaseUserManager):
    def create_user(self, sUserID, name, password = None):
        if not sUserID:
            raise ValueError('Users must have an ID')
 
        user = self.model(
            sUserID = sUserID,
            name = name,
            group = group,
            birthday = birthday,
            sex = sex,
            married = married,
            children = children,
            job = job,
            company = company,
            hobby = hobby,
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, sUserID, name, password):
        if not sUserID:
            raise ValueError('Users must have an ID')
 
        superUser = self.model(
            sUserID = sUserID,
            name = name,
        )
 
        superUser.set_password(password)
        superUser.is_admin = True
        superUser.save(using=self._db)
        return superUser

class SUser(AbstractBaseUser, PermissionsMixin):
    sUserID = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    group = models.CharField(max_length=5, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    married = models.CharField(max_length=5, blank=True, null=True)
    children = models.CharField(max_length=5, blank=True, null=True)
    job = models.CharField(max_length=128, blank=True, null=True)
    company = models.CharField(max_length=128, blank=True, null=True)
    hobby = models.CharField(max_length=128, blank=True, null=True)
    currentShot = models.IntegerField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = SUserManager()
    
    USERNAME_FIELD = 'sUserID'
    REQUIRED_FIELDS = ['name']
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
 
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
class Filtering(models.Model):
    sUserID = models.ForeignKey(SUser, on_delete=models.CASCADE, primary_key = True)
    serviceProvider = models.CharField(max_length=128)
    degree = models.CharField(max_length=64)
    price = models.CharField(max_length=64) 
        
class Survey(models.Model):
    sUserID = models.ForeignKey(SUser, on_delete=models.CASCADE)
    cID = models.IntegerField()
    shotID = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    fileName = models.CharField(max_length=256)
    preference = models.FloatField()
    reason = models.CharField(max_length=256)
    
    class Meta:
        unique_together = (("sUserID", "shotID"),)
        
class Group(models.Model):
    phone = models.CharField(max_length=20, blank=True, null=True)
    group = models.CharField(max_length=5, blank=True, null=True) 
    
class Clist(models.Model):
    CID = models.IntegerField(primary_key = True)
    Category = models.CharField(max_length=255, blank=True, null=True)
    ProgramNuame = models.CharField(max_length=255, blank=True, null=True)
    EpisodeNum = models.IntegerField()
    VideoURL = models.CharField(max_length=255, blank=True, null=True)
    VideoFileName = models.CharField(max_length=255, blank=True, null=True)
    VideoThumb = models.CharField(max_length=255, blank=True, null=True)
    FPS = models.FloatField()
    RegisterDateTime = models.DateTimeField()
    LastSavedDateTime = models.DateTimeField()
    TagStatus = models.IntegerField()
    User = models.CharField(max_length=255, blank=True, null=True)
    ProgramNameKor = models.CharField(max_length=255, blank=True, null=True)
    
class ShotInfo(models.Model):
    ShotID = models.IntegerField(primary_key = True)
    CID = models.ForeignKey(Clist, on_delete=models.CASCADE)
    ShotNum = models.IntegerField()
    StartFrame = models.IntegerField()
    EndFrame = models.IntegerField()
    ThumbURL = models.CharField(max_length=255, blank=True, null=True)
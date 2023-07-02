from django.db import models
from django.contrib.auth.models import User
import uuid 
# Create your models here.
class Profile(models.Model):
    author= models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    bio = models.TextField(max_length = 500,null=True,blank=True)
    short_intro = models.CharField(max_length = 200, null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True,default = 'profiles/user-default.png',upload_to="profiles/")
    social_github = models.CharField(max_length = 200,null=True,blank=True)
    location = models.CharField(max_length=200,null=True,blank=True)
    social_linkedin = models.CharField(max_length=200,null=True,blank=True)
    social_twitter = models.CharField(max_length=200,null=True,blank=True)
    social_youtube = models.CharField(max_length=200,null=True,blank=True)
    social_website = models.CharField(max_length=200,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
    @property
    def getUnreadMessages(self):
        unRead = self.message_set.filter(is_read == False).count()
        return unRead

    @property 
    def imageURL(self):
        try:
            url = self.profile_image.url 
        except:
            url = ""
        return url
    
class Skill(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=20000,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    
class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True)
    receiver = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True,related_name='receiver')
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False,editable=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read','-created']

    
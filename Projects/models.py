from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
import uuid
class Tags(models.Model):
    name = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_created=True,auto_now=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(null=True,blank=True,default="default.jpg",upload_to="")
    description = models.CharField(max_length=2000,null=True,blank=True)
    demo_link = models.CharField(max_length=20000,null=True,blank=True)
    source_link = models.CharField(max_length=20000,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    votes_ratio = models.IntegerField(default=0,null=True,blank=True)
    votes_count = models.IntegerField(default=0,null=True,blank=True)
    tags = models.ManyToManyField(Tags,blank=True)
    created = models.DateTimeField(auto_created=True,auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-votes_ratio','-votes_count','-created']
    
    @property
    def imageURL(self):
        try:
            url = self.featured_image.url 
        except:
            url = ""
        return url
    @property
    def getVoteCountAndRatio(self):
        totalVotes = self.review_set.all().count()
        upVotes = self.review_set.filter(value='up').count()
        ratio = (upVotes // totalVotes)*100
        self.votes_count = totalVotes
        self.votes_ratio = ratio
        print(self.votes_ratio)
        self.save()
    
    @property
    def feedbackers(self):
        lst = self.review_set.all().values_list('author__id',flat=True)
        return lst

class Review(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    VOTE_STATUS = (
        ('up','UP vote'),
        ('down','DOWN vote'),
    )
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    body = models.TextField(max_length=2000)
    value = models.CharField(max_length=5,choices=VOTE_STATUS,null=False,blank=False)
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    created = models.DateTimeField(auto_created=True,auto_now=True)
    def __str__(self):
        return self.project.title
    



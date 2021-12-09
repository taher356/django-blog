from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class PostModel(models.Model):

    image =models.ImageField(upload_to = 'blog/',default = 'blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tags
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.IntegerField(default=False)
    publish_date = models.DateTimeField(null =True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now =True)
    
    class Meta:
        ordering = ['create_date'] 
    
    def __str__(self):
        return "{}-{}".format(self.title,self.id)

    def snipets(self):
        return self.content[:99] +'...'    
    
    
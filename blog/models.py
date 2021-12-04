from django.db import models

# Create your models here.
class PostModel(models.Model):
    #image
    # author
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tags
    #category
    counted_view = models.IntegerField(default=0)
    status = models.IntegerField(default=False)
    publish_date = models.DateTimeField(null =True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now =True)
    
    class Meta:
        ordering = ['create_date'] 
    
    def __str__(self):
        return "{}-{}".format(self.title,self.id)
    
    
from django.db import models
from django.contrib.contenttypes.fields import ContentType #this is model class of content e,g: blog,tour
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from .signals import object_view_signal
from .utils import get_client_ip
from django.dispatch import receiver
from blog.models import Post,Category,Tag
from . import utils
# Create your models here.

class ObjectViewModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,  null=True,on_delete=models.SET_NULL)
    ip_address = models.CharField(max_length=100,blank=True,null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL,null=True) #ContentType is the model, like User,Post,Tour
    object_id = models.PositiveIntegerField() #object_id is the id os ContentType instance, like post.pk, tour.pk, user.id
    content_object = GenericForeignKey('content_type','object_id') # many to one relation between content_type and object_id
    time_stamp = models.DateTimeField( auto_now_add=True)

    class Meta:
        ordering = ['-time_stamp']

    def __str__(self):
        return f"{self.content_type}-{self.content_object}-{self.time_stamp}" 


@receiver(object_view_signal, sender=Post)
def post_viewed(sender,**kwargs):
    request = kwargs.get('request')
    instance = kwargs.get('instance')
    ip = get_client_ip(request)
    instance.view_count+=1;
    instance.save()
    #store the value in the session
    utils.recently_visited_posts(request=request, postid=instance.id)
    

@receiver(object_view_signal, sender=Category)
def category_viewed(sender, **kwargs):
    instance = kwargs.get('instance')
    instance.view_count+=1;
    instance.save()
    

@receiver(object_view_signal, sender=Tag)
def tag_viewed(sender, **kwargs):
    instance = kwargs.get('instance')
    instance.view_count+=1;
    instance.save()
    
    

    



    
    

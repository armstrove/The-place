from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


User = settings.AUTH_USER_MODEL


class ObjectViewed(models.Model):
    user               = models.ForeignKey(User, blank=True, null=True, on_delete='CASCADE') # user instance instance.id
    ip_address         = models.CharField(max_length=220, blank=True, null=True)
    content_type       = models.ForeignKey(ContentType, on_delete='CASCADE') # LanguageTests ,excersise, 
    object_id          = models.PositiveIntegerField()  # User id , product id ...
    content_object     = GenericForeignKey('content_type','object_id') # LanguageTest instance
    timestamp          = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s viewed %s" %(self.content_object, self.timestamp)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'
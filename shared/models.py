from django.db import models
import uuid
# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uid = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)


    class Meta:
        abstract = True
        ordering = ('id',)
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.
class PastedText(models.Model):
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    password=models.CharField(max_length=200,default='')
    text=RichTextField()
    created_at=models.DateTimeField(default=datetime.now)



from django.db import models
from . import views
# Create your models here.
class register(models.Model): 
 username = models.EmailField(max_length=50)
 password  = models.CharField(max_length=50)


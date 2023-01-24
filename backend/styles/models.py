from django.db import models
from authentication.models import User
# Create your models here.
class styles(models.Model):
    
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Change_the_main_color_theme=models.CharField(max_length=255)
   

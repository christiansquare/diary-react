from django.db import models
from authentication.models import User

# Create your models here.
class moodtracker(models.Model):
    emoji = models.CharField(max_length=255)
    date= models.CharField(max_length=255)
    journal_entry = models.CharField(max_length=255)
    User = models.ForeignKey(User, on_delete=models.CASCADE)


    
    
    
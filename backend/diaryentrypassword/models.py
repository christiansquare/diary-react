from django.db import models
from authentication.models import User
# Create your models here.
class diaryentrypassword(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Password=models.CharField(max_length=255)
   
    
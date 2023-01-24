from rest_framework import serializers
from .models import diaryentrypassword

class diaryentrypasswordserializer(serializers.ModelSerializer):
    class Meta:
    model = diaryentrypassword
    fields =['id', 'Password','User_id']
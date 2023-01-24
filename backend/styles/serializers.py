from rest_framework import serializers
from .models import styles

class stylesserializer(serializers.ModelSerializer):
    class Meta:
        model=styles
        fields=['id', 'Change_the_main_color_theme', 'User_id']
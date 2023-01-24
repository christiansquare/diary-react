from rest_framework import serializers
from .models import moodtracker

class moodtrackerserializer(serializers.ModelSerializer):
    class Meta:
        model= moodtracker
        fields = ['id', 'emoji', 'date', 'journal_entry', 'User_id',]
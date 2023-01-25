from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import moodtrackerserializer
from . models import moodtracker

@api_view(['GET', 'POST'])
def moodtracker_list(request):

    if request.method == 'GET':  
     moodtracker98 = moodtracker.objects.all()
     serializers = moodtrackerserializer(moodtracker98, many = True)
     return Response(serializers.data)
    elif request.method == 'POST':
        serializers=moodtrackerserializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def moodtracker_detail(request,pk):
    moodtracker988= get_object_or_404(moodtracker, pk=pk)
    if request.method == 'GET':
        serializers = moodtrackerserializer(moodtracker988);
        return Response (serializers.data)
    elif request.method == 'PUT':
        serializers = moodtrackerserializer(moodtracker988, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    elif request.method =='DELETE':
        moodtracker988.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

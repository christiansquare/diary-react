from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import diaryentrypasswordserializer
from .models import diaryentrypassword


@api_view(['GET', 'POST'])
def diaryentrypassword_list(request):

    if request.method == 'GET':  
     diaryentrypassword1 = diaryentrypassword.objects.all()
     serializers = diaryentrypasswordserializer(diaryentrypassword1, many = True)
     return Response(serializers.data)
    elif request.method == 'POST':
        serializers=diaryentrypasswordserializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def diaryentrypassword_detail(request,pk):
    diaryentrypassword988 = get_object_or_404(diaryentrypassword, pk=pk)
    if request.method == 'GET':
        serializers = diaryentrypasswordserializer(diaryentrypassword988);
        return Response (serializers.data)
    elif request.method == 'PUT':
        serializers = diaryentrypasswordserializer(diaryentrypassword988, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    elif request.method =='DELETE':
        diaryentrypassword988.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


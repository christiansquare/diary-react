from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import stylesserializer
from .models import styles


@api_view(['GET', 'POST'])
def styles_list(request):

    if request.method == 'GET':  
     styles98 = styles.objects.all()
     serializers = stylesserializer(styles98, many = True)
     return Response(serializers.data)
    elif request.method == 'POST':
        serializers=stylesserializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def styles_detail(request,pk):
    styles988= get_object_or_404(styles, pk=pk)
    if request.method == 'GET':
        serializers = stylesserializer(styles988);
        return Response (serializers.data)
    elif request.method == 'PUT':
        serializers = stylesserializer(styles988, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    elif request.method =='DELETE':
        styles988.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




from django.shortcuts import render

from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import generics

from .models import Parent,Children
from .serializer import ParentSerializer, ChildrenSerializer
from rest_framework import status
from functools import wraps
# Create your views here.

class ParentViewSet(generics.ListAPIView):
    serializer_class = ParentSerializer

    def get_queryset(self):

        
        return Parent.objects.all()

    def post (self, request,format = None):
        serializer = ParentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

def resource_checker(model):
    def check_entity(fun):
        @wraps(fun)
        def inner_fun(*args, **kwargs):
            try:
                x = fun(*args, **kwargs)
                return x
            except model.DoesNotExist:
                return Response({'message': 'Not Found'}, status = status.HTTP_204_NO_CONTENT )
        return inner_fun
    return check_entity       
class ParentDetailView (APIView):
    @resource_checker(Parent)
    def get (self,request,pk, format = None):
        queryset = Parent.objects.get(pk = pk)
        serializer = ParentSerializer(queryset)
        return Response(serializer.data)
    @resource_checker(Parent)
    def put (self,request,pk, format = None):
        queryset = Parent.objects.get(pk = pk)
        serializer = ParentSerializer(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    @resource_checker(Parent)
    def delete (self,request,pk, format = None):
        queryset = Parent.objects.get(pk = pk)
        queryset.delete()
        return Response( status = status.HTTP_204_NO_CONTENT) 


class ChildrenViewSet(generics.ListAPIView):
    serializer_class = ChildrenSerializer

    def get_queryset(self):        
        return Children.objects.all()

    def post (self, request,format = None):
        serializer = ChildrenSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ChildrenDetailView (APIView):
    @resource_checker(Children)
    def get (self,request,pk, format = None):
        queryset = Children.objects.get(pk = pk)
        serializer = ChildrenSerializer(queryset)
        return Response(serializer.data)

    @resource_checker(Children)
    def put (self,request,pk, format = None):
        queryset = Children.objects.get(pk = pk)
        serializer = ChildrenSerializer(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    @resource_checker(Children)
    def delete (self,request,pk, format = None):
        queryset = Children.objects.get(pk = pk)
        queryset.delete()
        return Response( status = status.HTTP_204_NO_CONTENT) 



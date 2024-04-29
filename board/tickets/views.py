from django.shortcuts import render 
from django.http import response
from rest_framework.decorators import api_view
from  rest_framework import status,filters
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import Http404
# Create your views here.

#1.function based views FBV
#1.1 GET POST
#from rest_framework.decorators import api_view
#from  rest_framework import status,filters
#from rest_framework.response import Response
@api_view(['GET','POST'])
def FBV_List(request):
    if request.method=='GET':
        guests=Guest.objects.all()
        serializer=GuestSerializers(guests,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=GuestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.data,status.HTTP_400_BAD_REQUEST)
         
@api_view(['GET','PUT','DELETE'])
def get_pk(request,pk):
    try:
        guests=Guest.objects.get(pk=pk)
    except guests.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #Get
    if request.method=='GET':
         serializer=GuestSerializers(guests)
         return Response (serializer.data)
    #PUT
    elif request.method=='PUT':
        serializer=GuestSerializers(guests,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        guests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#2.Class based views CBV
#2.2 GET POST
from rest_framework.views import APIView
class CBV_List(APIView):
    def get(self,request):
        guest=Guest.objects.all()
        serializer=GuestSerializers(guest,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=GuestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)

#4.2 GET PUT Delete class based views pk 
class CBV_Pk(APIView):
    def get (self ,request,pk):
        try:
             guests=Guest.objects.get(pk=pk)
             serializer=GuestSerializers(guests)
             return Response(serializer.data,status=status.HTTP_200_OK)
        except Guest.DoesNotExist:
            raise Http404
        
    def put (self,request,pk):
        guests=Guest.objects.get(pk=pk)
        serializer=GuestSerializers(guests,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
       try:
           guests=Guest.objects.get(pk=pk)
           guests.delete()
       except Guest.DoesNotExist:
           raise Http404

#or we can do it like that 
class CBV_pk2(APIView):
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        try:
            guests=self.get_object(pk)
            serializer=GuestSerializers(guests)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Guest.DoesNotExist:
            raise Http404
    def put(self,request,pk):
        guests=self.get_object(pk)
        serializer=GuestSerializers(guests,data=request.data)
        if  serializer.data.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_304_NOT_MODIFIED)
    def delete(self,request,pk):
        guests=self.get_object(pk)
        guests.delete()
        return Response(status=status.HTTP_200_OK)
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User 
from django.http import JsonResponse,HttpResponse
from .models import *

def hello(request):
    # Your view logic here
    data = {'message': 'Hello, world!'}
    return JsonResponse(data)
def home(request):
    board=Board.objects.all()
    board_name=[]
    for i in board:
        board_name.append(i.description)
    return render (request,'home.html',{"boards":board})
def getborad(request,board_id):
    
    board=Board.objects.get(pk=board_id)
    
    return render(request,'home.html',{"board":board})
def new_topic(request,board_id):
    board=Board.objects.get(pk=board_id)
    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['message']
        user=User.objects.first()
        topic=Topic.objects.create(subject=subject,
                                   board=board,
                                   created_by=user)
        post=Posts.objects.create(message=message,
                                  topic=topic,
                                  created_by=user)
        return redirect('getborad',board_id=board.pk)
    return render(request,'new_topic.html',{"board":board})
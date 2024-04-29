
from django.urls import path ,include
from . import views
urlpatterns = [
    
    path('',views.home,name="home"),
    path('bord/<int:board_id>',views.getborad,name="getborad"),
    path('bord/<int:board_id>/new/',views.new_topic,name="new_topic"),
]

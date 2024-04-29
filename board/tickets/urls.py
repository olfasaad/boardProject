from django.urls import path
from . import views
urlpatterns=[
    path("api/",views.FBV_List),
    path("api2/<int:pk>/",views.get_pk),
    path("api3/",views.CBV_List.as_view()),
    path("api4/<int:pk>/",views.CBV_Pk.as_view()),
    path('api5/<int:pk>/',views.CBV_pk2.as_view()),
]

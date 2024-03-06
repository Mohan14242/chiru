from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('name/<str:pk>/',views.name,name='name'),
    path('create_room/',views.createroom,name='room'),
    
] 
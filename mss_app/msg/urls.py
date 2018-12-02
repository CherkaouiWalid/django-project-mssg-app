from  django.urls import path

from . import views

urlpatterns=[path('',views.msg , name='msg'),
             path('create/', views.createMsg, name='createMsg'),
             path('sent/', views.sentmsg , name ='sentMsg')
             ]
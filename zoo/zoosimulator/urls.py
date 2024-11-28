from django.urls import path
from . import views

#First path specifies that http://127.0.0.1:8000/zoosimulator will display the home view
#Other paths route HTTP requests linking the buttons in template to their associated view
urlpatterns = [
    path('', views.zoo_home, name='zoo_home'),
    path('pass_time/', views.pass_time, name='pass_time'),
    path('feed_zoo/', views.feed_zoo, name='feed_zoo'),
]


    
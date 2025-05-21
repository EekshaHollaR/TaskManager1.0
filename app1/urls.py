from django.urls import path
from . import views

urlpatterns=[
    path('',views.rootPageView,name='rootPage'),
    path('indexPage/', views.IndexView, name='indexPage'),
    path('tasks/<str:day>/',views.dayView,name="dayView")
]

 

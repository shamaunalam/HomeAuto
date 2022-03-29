from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home),
    path('device/<str:pk>',views.getdevicestatus),
    path('device/<str:pk>/light',views.togglelight),
    path('device/<str:pk>/fan',views.togglefan),
]

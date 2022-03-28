from posixpath import basename
from django.urls import path, include
from .views import SingerView

urlpatterns = [
    path('', SingerView.as_view()),

    
    
]
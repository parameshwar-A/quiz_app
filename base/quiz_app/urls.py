from django.urls import path
from quiz_app import views as quiz_views

urlpatterns = [
        path('', quiz_views.home),
        ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.moodtracker_list),
    path('<int:pk>/',views.moodtracker_detail),
]
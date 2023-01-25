from django.urls import path
from . import views

urlpatterns = [
    path('', views.styles_list),
    path('<int:pk>/',views.styles_detail),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.diaryentrypassword_list),
    path('<int:pk>/',views.diaryentrypassword_detail),
]

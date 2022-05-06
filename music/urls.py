from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.music_detail),
    path('', views.music_list),
]
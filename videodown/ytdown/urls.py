from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="yt_home"),
    path('detail/', views.detail, name='yt_detail'),
    path('download/', views.yt_download, name='yt_download'),
]
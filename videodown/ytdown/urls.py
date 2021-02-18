from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="yt_home"),
    path('download/', views.yt_download, name='yt_download')
]
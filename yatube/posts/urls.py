from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.index),
    path('group/<slug:slug>/', views.group_posts, name='groups'),

]

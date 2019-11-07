from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('birthdays/<int:person_id>/', views.detail, name='detail'),
    path('all/', views.all, name='all'),
    path('new/', views.new, name='new')
]

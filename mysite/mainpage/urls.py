from django.urls import  path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='home'),
    path('first_page', views.first, name='first'),
    path('second_page', views.second, name='second'),
    path('third_page', views.third, name='third'),
    path('check', views.check, name='check'),
    path('register/', views.register, name='register'),
    path('base/<pk>/bookmark/', login_required(views.BookmarkView.as_view()), name='bookmark'),
    path('base/', views.base_home, name='base_home'),
    path("add", views.create, name='create'),
]

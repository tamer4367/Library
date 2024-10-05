from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create-book',views.BookCreate.as_view(),name='create-book'),
    path('detail/<int:pk>',views.BookDetail.as_view(),name='detail'),
    path('accounts/register',views.Register.as_view(),name='register'),
    ]
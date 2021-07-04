from django.urls import path

from todo_list import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<id>', views.delete, name='delete'),
    path('crossoff/<id>', views.crossoff, name='crossoff'),
    path('uncross/<id>', views.uncross, name='uncross'),
    path('edit/<id>', views.edit, name='edit'),
]

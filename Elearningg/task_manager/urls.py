from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_task/', views.add_task, name='add_task'),
    path('done/<int:id>/', views.done_btn, name='done_btn'),
    path('delete/<int:id>/', views.delete_btn, name='delete_btn'),
    path('edit/<int:id>/', views.edit_btn, name='edit_btn'),
]
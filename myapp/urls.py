from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('save-data/', views.save_data, name='save_data'),


# --------------- TEACHER ---------------
    path('add-teacher/', views.add_teacher, name='add_teacher'),
]
from django.urls import path
from . import views


urlpatterns = (
    path('',views.index, name='form_input'),
    path('success/', views.success, name='success'),
    path('teacher/', views.teacher, name='teacher'),
    path('teacher/<str:dept>', views.teacher),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('generate/', views.generate, name='generate'),


)

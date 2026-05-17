from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('index/', views.gretting, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),


    path('forgot_password/', views.reset_password_view, name='forgot_password'),
    path('password_reset_done/', views.custom_password_reset_done, name='password_reset_done'),

    path('reset/<uidb64>/<token>/', views.custom_password_reset_confirm, name='custom_password_reset_confirm'),
    path('reset/done', views.password_reset_complete, name='password_reset_complete'),

    path('userprofile/', views.user_profile, name='userprofile'),

    

]
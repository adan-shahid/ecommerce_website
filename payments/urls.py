from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.create_checkout_session, name='create_checkout_session'),
    

]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ajouter_appeloffre', views.add, name="ajouter_appeloffre"),
    path('update_appeloffre/<str:pk>', views.update, name="update_appeloffre"),
    path('supp_appeloffre/<str:pk>', views.supp, name="supp_appeloffre"),
    path('postulation/<str:pk>', views.add_postule, name="postulation"),
    path('postes', views.aff_postule, name="aff_postule"),
    path('supp_appeloffre/<str:pk>', views.supp_postule, name="supp_poste"),
    path('update_postule/<str:pk>', views.update_postule, name="update_postule"),
    path('registre', views.register, name="registre"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('profile', views.profile, name="profile"),
    path('all_user', views.aff_user, name='aff_user'),
    path('un_user', views.aff_un_user, name='aff_un_user'),

]

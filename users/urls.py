from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.profiles,name="profiles"),
    path('profile/<str:pk>',views.userProfile,name="user-profile"),
    path('createSkill/',views.createSkill,name="createSkill"),
    path('updateSkill/<str:pk>',views.updateSkill,name="updateSkill"),
    path('deleteSkill/<str:pk>',views.deleteSkill,name="deleteSkill"),
    path('login/',views.loginView,name="login"),
    path('logout/',views.logoutView,name="logout"),
    path('register/',views.registerView,name="register"),
    path('account/',views.userAccount,name="account"),
    path('edit-profile/',views.updateProfile,name="edit-account"),
    path('deleteProfile/<str:pk>',views.deleteProfile,name="deleteProfile"),
    path('inbox/',views.inbox,name="inbox"),
    path('createMessage/<str:pk>',views.createMessage,name="createMessage"),
    path('viewMessage/<str:pk>',views.viewMessage,name="message"),
]
from django.urls import path,include 
from . import views
urlpatterns = [
    path('',views.projectsPage,name="projects"),
    path('project/<str:pk>',views.projectPage,name="project"),
    path('createProject/',views.createProject,name="createProject"),
    path('deleteProject/<str:pk>',views.deleteProject,name="deleteProject"),
    path('updateProject/<str:pk>',views.updateProject,name="updateProject"),
    path('createTag/',views.createTag,name="createTag"),
] 

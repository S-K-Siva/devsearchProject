from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.getRoutes,name="apiRoutes"),
    path('projects/',views.getProjects,name="Projects"),
    path('profiles/',views.getProfiles,name="profiles"),
    path('project/<str:pk>',views.getProject,name="Project"),
    path('profile/<str:pk>',views.getProfile,name="Profile"),
    path('project/<str:pk>/upvote',views.upVote,name="upVote"),
    path('project/<str:pk>/downvote',views.downVote,name="downVote"),
    path('deleteTag/',views.deleteTag,name="deleteTag"),
]
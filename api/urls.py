from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.getRoutes,name="APIapiRoutes"),
    path('projects/',views.getProjects,name="APIProjects"),
    path('profiles/',views.getProfiles,name="APIprofiles"),
    path('project/<str:pk>',views.getProject,name="APIProject"),
    path('profile/<str:pk>',views.getProfile,name="APIProfile"),
    path('project/<str:pk>/upvote',views.upVote,name="APIupVote"),
    path('project/<str:pk>/downvote',views.downVote,name="APIdownVote"),
    path('deleteTag/',views.deleteTag,name="APIdeleteTag"),
]
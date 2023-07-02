from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from Projects.models import Project, Review, Tags
from users.models import Profile
from .serializers import ProjectSerializer,ProfileSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'api/projects'},
        {'GET':'api/projects/:id'},
        {'POST':'api/project/:id/upvote'},
        {'POST':'api/project/:id/downvote'},
        {'POST':'api/users/token'},
        {'POST':'api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
# @permission_classes([IsAuthenticated]) #this is how we put restriction on api views.
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile,many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upVote(request,pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    
    review, created = Review.objects.get_or_create(
        author=user,
        project=project,
    )
    review.value="up"
    review.save()
    project.getVoteCountAndRatio

    serializer = ProjectSerializer(project,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def downVote(request,pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    
    review, created = Review.objects.get_or_create(
        author=user,
        project=project,
    )
    review.value="down"
    review.save()
    project.getVoteCountAndRatio

    serializer = ProjectSerializer(project,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTag(request):
    projectId = request.data['project'];
    tagId = request.data['tag'];

    project = Project.objects.get(id=projectId);
    tag = Tags.objects.get(id=tagId);

    project.tags.remove(tag);

    return Response("Tag is deleted!");





from .models import Profile,Skill 
from django.db.models import Q 
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def searchProfiles(request):
    search_query=""
    if request.method == "GET":
        search_query = request.GET.get("search_query","")
    
    skills = Skill.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
    Q(skill__in=skills) | Q(name__icontains=search_query) | Q(bio__icontains = search_query) | Q(bio__icontains =search_query)
    )
    print(profiles,search_query)
    return profiles, search_query


def getPagination(request,profiles):
    page = 1
    if request.GET.get('page'):
        page = request.GET.get('page')
    totalInstances = 6
    paginator = Paginator(profiles,totalInstances)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        profiles = paginator.page(paginator.num_pages + 1)
    
    leftIndex = int(page) - 2
    rightIndex = int(page) + 3
    if leftIndex < 1:
        leftIndex = 1
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    count_range = range(leftIndex,rightIndex)
    return paginator,count_range,profiles 
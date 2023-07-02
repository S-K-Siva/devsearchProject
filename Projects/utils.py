from django.db.models import Q
from .models import Project,Tags,Review
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def searchProjects(request):
    search_query=""
    if request.method == "GET":
        search_query = request.GET.get("search_query","")


    print(search_query)
    tags = Tags.objects.filter(name__icontains = search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) | Q(author__username__icontains=search_query)|Q(tags__in=tags)|Q(description__icontains=search_query)
    )
    
    return projects,search_query

def getPagination(request,projects):
    projects = projects
    page = 1
    if request.GET.get('page'):
        page = request.GET.get('page')
    
    
    totalInstances = 3
    paginator = Paginator(projects,totalInstances)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)


    leftIndex = int(page) - 4
    rightIndex = int(page) + 3
    if leftIndex < 1:
        leftIndex = 1
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages+1
    
    count_range = range(leftIndex,rightIndex)
    return paginator,count_range,projects
from django.shortcuts import render, redirect
from .models import Project,Review,Tags
from .forms import ProjectForm,ReviewForm,TagForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects,getPagination
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def projectsPage(request):
    projects,search_query = searchProjects(request)
    paginator,count_range,projects = getPagination(request,projects)
    return render(request,'Projects/projects.html',{"projects":projects,"search_query":search_query,"paginator":paginator,"count_range":count_range})

def projectPage(request,pk):
    form = ReviewForm()
    project = Project.objects.get(id=pk)
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user.profile
            review.project = project
            review.save()
            project.getVoteCountAndRatio
            
            return redirect('project',project.id)
    print(project.feedbackers)
    return render(request,'Projects/project.html',{"project":project,'reviewers':project.feedbackers,'form':form})


#create project
@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            tagList = Project(title=project.title,id=project.id,author=request.user,description=project.description,demo_link=project.demo_link,source_link=project.source_link,votes_count=project.votes_count,votes_ratio=project.votes_ratio)
            tagList.save()
            tags = list(request.POST.get('new_tag').strip().split(','))
            if tags[0] != "" :
                for tag in tags:
                    tag, created = Tags.objects.get_or_create(name=tag)
                    tagList.tags.add(tag)
            if request.FILES:
                print("YES, file is there",request.FILES['featured_image'])
                tagList.featured_image = request.FILES['featured_image']
            tagList.save()
            
        return redirect("projects")
    return render(request,"Projects/project_form.html",{"form":form})

#update project
@login_required(login_url="login")
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            project = form.save(commit=False)
            tags = list(request.POST.get('new_tag').strip().split(','))
            if tags[0] != "" :
                for tag in tags:
                    tag, created = Tags.objects.get_or_create(name=tag)
                    project.tags.add(tag)
            
        return redirect("projects")

    return render(request,"Projects/project_form.html",{"form":form,"projectId":pk,"project":project})
   
@login_required(login_url="login")
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        if request.POST.get('sure') == "submit":
            project.delete()
        return redirect("projects")
    return render(request,"Projects/delete_project.html",{"project":project})

@login_required(login_url="login")
def createTag(request):
    form = TagForm()
    if request.method == "POST":
        form = TagForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render("projects")
    return render(request,"Project/create_project.html",{"form":form})
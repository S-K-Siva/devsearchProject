from django.shortcuts import render,redirect
from .models import Profile,Skill, Message
from Projects.models import Project
from .forms import SkillForm, customUserCreationForm,ProfileForm,MessageForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from .utils import searchProfiles,getPagination
# Create your views here.

def loginView(request):
    if request.method == "POST":
        userName = request.POST["username"]
        passWord = request.POST["password"]
        # checking whether the user exist or not

        try:
            user = User.objects.get(username=userName)
        except:
            messages.error(request,"Username doesn't exist!")
            return redirect('login')
        user = authenticate(request,username=userName,password=passWord)
        if user is not None:
            # user exists!
            login(request,user)
            messages.success(request,"User loggedIn successfully!")
            return redirect("profiles")
        else:
            messages.error(request,"Username or password is incorrect")
            return redirect('login')
    return render(request,'users/login_register.html')
@login_required(login_url="login")
def logoutView(request):
    logout(request)
    return redirect('login')

def registerView(request):
    form = customUserCreationForm()
    if request.method == "POST":
        print(request.POST)
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # login(request,user)
            messages.success(request,"User Created Successfully!")
            return redirect('login')
        else:
            messages.error(request,"Error has occurred while registering!")
            
        
    return render(request,'users/login_register.html',{"form":form,"page":"register"})
def profiles(request):
    profiles,search_query = searchProfiles(request)
    paginator,count_range,profiles = getPagination(request,profiles)
    return render(request,'users/profiles.html',{'profiles':profiles,'search_query':search_query,'paginator':paginator,'count_range':count_range})


@login_required(login_url="login")
def inbox(request):
    Allmessages = Message.objects.filter(receiver=request.user.profile)
    unreadCount = Allmessages.filter(is_read=False).count()
    return render(request,"users/inbox.html",{"messages":Allmessages,"unreadCount":unreadCount})

@login_required(login_url='login')
def createMessage(request,pk):
    form = MessageForm()
    receiver = Profile.objects.get(id=pk)
    if request.method == "POST":
        form = MessageForm(request.POST)
        message = form.save(commit=False)
        message.sender = request.user.profile
        message.receiver = receiver
        message.is_read = False
        message.name = message.sender.name
        message.save()
        return redirect('user-profile',receiver.id)
    return render(request,'users/message_form.html',{'form':form,'receiver':receiver})

@login_required(login_url = 'login')
def viewMessage(request,pk):
    message = Message.objects.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    return render(request,"users/message.html",{"message":message})
@login_required(login_url="login")
def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description="")
    otherSkills = profile.skill_set.filter(description="")
    projects = Project.objects.filter(author=profile.author)
    print(projects)
    return render(request,'users/user-profile.html',{'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills,'projects':projects})


@login_required(login_url="login")
def updateProfile(request):
    user = request.user
    profile = user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            # profile = form.save(commit=False)
            form.save()
            
            # if request.FILES:
            #     profile.profile_image = request.FILES['profile_image']
            
        return redirect('account')
    return render(request,"users/profile_form.html",{"form":form})
@login_required(login_url="login")
def deleteProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()
    return render(request,"users/skill_form.html",{"skill":profile.author.username})
@login_required(login_url="login")
def createSkill(request):
    form = SkillForm()
    
    if request.method == "POST":
        form = SkillForm(request.POST)
        print(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.author = request.user.profile
            skill.save()
        
        return redirect("account")
    return render(request,'users/skill_form.html',{"form":form})
@login_required(login_url="login")
def updateSkill(request,pk):
    skill = Skill.objects.get(id=pk)
    form = SkillForm(instance=skill)
    
    if request.method == "POST":
        form = SkillForm(request.POST,instance=skill)
        print(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect("account")
    return render(request,'users/skill_form.html',{"form":form})
@login_required(login_url="login")
def deleteSkill(request,pk):
    skill = Skill.objects.get(id=pk)
    if request.method == "POST":
        skill.delete()
        return redirect("account")
    return render(request,'users/skill_form.html',{"skill":skill})

@login_required(login_url="login")
def userAccount(request):
    user = request.user
    profile = user.profile 
    projects = Project.objects.filter(author=user)
    skills = Skill.objects.filter(author=profile)
    return render(request,"users/account.html",{"profile":profile,"projects":projects,"skills":skills})
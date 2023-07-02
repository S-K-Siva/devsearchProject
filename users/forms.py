from django import forms 
from .models import Skill,Profile, Message
from django.forms import ModelForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
class SkillForm(forms.Form,forms.ModelForm):
    
    class Meta:
        model = Skill 
        fields = '__all__'
        exclude = ['author','created','id']
    
    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({"class":"input"})


class ProfileForm(ModelForm,forms.Form):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["author","created","id"]
    
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({"class":"input"})

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']
        labels = {
            'first_name':'Name',
            
        }
    def __init__(self,*args,**kwargs):
        super(customUserCreationForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            if name == 'password1':
                field.widget.attrs.update({"name":"password"})
            elif name == "password2":
                field.widget.attrs.update({"name":"confirmPassword"})
            field.widget.attrs.update({"class":"input"})


class MessageForm(ModelForm,forms.Form):

    class Meta:
        model = Message
        fields = "__all__"
        exclude = ['sender','receiver','id','created']
    
        # label = {
        #     'subject':'Subject',
        #     'body':'Content',
        # }
    

    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
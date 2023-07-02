from django.forms import ModelForm 
from .models import Project,Review,Tags
from django import forms

class ProjectForm(ModelForm,forms.Form):
    new_tag = forms.CharField(label="Tag",max_length=200,required=False)
    
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ["id","created","Tag","author","tags"]
       
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({"class":"input"})

class ReviewForm(ModelForm):
    class Meta:
        model = Review 
        fields = ['value','body']
       
    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({"class":"input"})
        
class TagForm(ModelForm):
    class Meta:
        model = Tags 
        fields = '__all__'
       
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(),widget=forms.CheckboxSelectMultiple)
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({"class":"input"})
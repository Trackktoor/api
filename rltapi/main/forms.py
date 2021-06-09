from django import forms

class ProjectForm(forms.Form):
    Name = forms.CharField(max_length=155)
    TaskType = forms.CharField(max_length=155)
    ProjectType = forms.IntegerField()
    ShortTask = forms.CharField(max_length=155)
    CreateDate = forms.DateTimeField()
    Description = forms.CharField(max_length=255)
    ProjectLink = forms.CharField(max_length=255)
    Photos = forms.CharField(max_length=255)
from django import forms
from .models import Project,Ratings

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')


class NewProjectForm(forms.ModelForm):
    class Meta:
      model = Project
      fields = ['profile','image','title','description','link']
        

class RatingForm(forms.ModelForm):
  class Meta:
    model = Ratings
    fields = ['design','usability','content',]
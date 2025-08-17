from django.forms import ModelForm
from django import forms
from .models import JobPost,JobApplication

class JobPostingForm(ModelForm):
    class Meta:
        model = JobPost
        fields = '__all__'

class JobApplicationForm(ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'
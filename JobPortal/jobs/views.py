from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
# Create your views here.

class JobPosting(View):
     def get(self,request):
          if request.user.is_authenticated and request.user.user_type =='E':
               
               form = JobPostingForm()
               context={
                    'form':form
               }
               return render(request,'jobs/job_post.html',context)
          else:
              messages.error(request,"Only Employer can post Jobs")
              return redirect('home')
     def post(self,request):
         form = JobPostingForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('home')
         else:
            context={
               'form':form
             }
            return render(request,'jobs/job_post.html',context)  
         

class JobApplying(View):
     def get(self,request):   
          if  request.user.is_authenticated and request.user.user_type =='S' :
               form = JobApplicationForm()
               context={
                    'form':form
               }
               return render(request,'jobs/apply_for_job.html',context)
          else:
              messages.error(request,"Only seekers can apply for jobs")          
              return redirect('home')
     def post(self,request):
         form = JobApplicationForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('home')
         else:
            context={
               'form':form
             }
            return render(request,'jobs/apply_for_job.html',context)  
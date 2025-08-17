from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('post-job/',JobPosting.as_view(),name="post_job"),
    path('apply_for_job/',JobApplying.as_view(),name="apply_for_job")
]

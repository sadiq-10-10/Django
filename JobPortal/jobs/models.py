from django.db import models
from accounts.models import User
# Create your models here.
class JobPost(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50, choices=(
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Other', 'Other'),
    ))
    posted_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.job_title} at {self.employer.company_name}"


class JobApplication(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    seeker = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='applications/', blank=True)
    cover_letter = models.TextField(blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.seeker.full_name} applied for {self.job.job_title}"

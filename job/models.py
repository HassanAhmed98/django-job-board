from django.db import models

# Create your models here.

JOB_TYPE = (
    ('full time', 'full time'),
    ('part time', 'part time'))
class Job(models.Model):
    title = models.CharField(max_length=100) #column
    #location
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    discription = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experieance = models. IntegerField(default=1)
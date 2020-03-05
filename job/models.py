from django.db import models

from users.models import User

class Job(models.Model):
    title = models.CharField(max_length=220)
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=220)
    location = models.CharField(max_length=220)
    qualification = models.CharField(max_length=255)
    experience_year  = models.IntegerField()
    salary  = models.IntegerField()
    job_type = models.CharField(max_length=255)
    deadline = models.DateField()
    skills = models.TextField()
    
    class Meta:
        db_table = 'job_job'
        
    def __str__(self):
        return self.title
    
class JobRating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job  = models.ForeignKey(Job,on_delete=models.CASCADE)
    rating = models.IntegerField()
    
    def __str__(self):
        return f'User - {self.user.username} && Job - {self.job.title} && Rating- {self.rating}'
    
class JobReview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job  = models.ForeignKey(Job,on_delete=models.CASCADE)
    review = models.TextField()
    
    def __str__(self):
        return f'User - {self.user.username} && Job - {self.job.title}'

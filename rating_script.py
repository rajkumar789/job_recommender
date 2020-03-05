import os 
import django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_system.settings')
django.setup()

from  job.models import Job, JobRating
from users.models import User 
import random 

users = User.objects.all()
user_ids = []
for user in users:
    user_ids.append(user.id)
jobs = Job.objects.all()


for job in jobs:
    JobRating.objects.create(
        user_id = random.choice(user_ids),
        job  = job ,
        rating = random.randint(1,5)
    )
print("RAting is done Successfully")
    
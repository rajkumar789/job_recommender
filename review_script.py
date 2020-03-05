import os
import django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_system.settings')
django.setup()

import random 
from faker import Faker 
from users.models import User 
from job.models import JobReview,Job

users = User.objects.all()
user_ids = []
for user in users:
    user_ids.append(user.id)
jobs = Job.objects.all()

fake = Faker()

for job in jobs:
    JobReview.objects.create(
        user_id = random.choice(user_ids),
        job  = job ,
        review = fake.text()
    )
print("Review is Recorded Successfully ")
    
    

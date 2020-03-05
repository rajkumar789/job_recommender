# "pip install Faker" to install Faker 
import os
import django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_system.settings')
django.setup()

from job.models import Job 
from faker import Faker
import datetime
import random 


import csv 
'''
    #Csv File Includes 
    image 
    title
    location
    category
    job_type 
    
'''
    
fake = Faker()
fake.date_between(start_date='today', end_date='+30y')
fake.date_time_between(start_date='-30y', end_date='now')
start_date = datetime.date(year=2020, month=1, day=1)


with open('job_dataset.csv','r') as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
        tt = line['title']
        j = Job.objects.create(
                title = line['title'],
                description = f'Job vacancy on {tt}',
                category = line['category'],
                qualification = "Well Known Experience On Programming",
                location = line['location'],
                experience_year = random.randint(1,5),
                salary = random.randint(25000,50000),
                job_type  = line['job_type'],
                deadline = fake.date_between(start_date=start_date, end_date='+30y')
                
            )
    print("done")
        
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .forms import *

@csrf_exempt
def AddJoB(request):
    form = JobModelForm()
    jobs  = Job.objects.all()

    
    if request.method == 'POST':
        form = JobModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list_job')
       
            
    context = {
        'form': form
    }
    return render(request,'add_job.html',context)

def ListJob(request):
    jobs  = Job.objects.all()
    paginator = Paginator(jobs,9)
    page = request.GET.get('page',1)
    jobs = paginator.get_page(page)
    context = {
        'jobs':jobs
    }
    return render(request,'list_job.html',context)

def JobDetailView(request,id):
    job  = Job.objects.get(id=id)
    print(job)
    context = {
        'job': job
    }
    return render(request,'detail_job.html',context)

def ReviewMovie(request,movie_id):
    job_rating = JobRating.objects.create(
        user = request.user,
        job_id = movie_id,
        rating = request.POST['rating']
        )
    job_review = JobReview.objects.create(
                   user = request.user,
                   job_id  = movie_id,
                   review = request.POST['comment'] 
                )
    
    if job_rating and job_review:
        return redirect('/list_job')

from django.contrib import admin
from django.urls import path

from employee.views import HomePage, EmployeeList, \
EmployeAdd, EmployeDelete
from employer.views import EmployerList

from users.views import Register, Login,LogoutUser
from job.views import AddJoB,ListJob,JobDetailView,ReviewMovie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage),
    path('employee', EmployeeList),
    path('employer', EmployerList),
    path('employee-add', EmployeAdd),
    path('employee-delete', EmployeDelete),

    path('register/', Register),
    path('login/', Login),
    path('logout/', LogoutUser),
    path('add_job',AddJoB),
    path('list_job',ListJob),
    path('job_detail/<int:id>',JobDetailView),
    path('review_movie/<int:movie_id>',ReviewMovie)


]

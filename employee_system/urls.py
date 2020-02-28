
from django.contrib import admin
from django.urls import path

from employee.views import HomePage, EmployeeList, \
EmployeAdd, EmployeDelete
from employer.views import EmployerList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage),
    path('employee', EmployeeList),
    path('employer', EmployerList),
    path('employee-add', EmployeAdd),
    path('employee-delete', EmployeDelete),
]

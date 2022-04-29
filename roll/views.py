from django.shortcuts import render,HttpResponse
from .models import *
from .forms import EmployeeForm,FilterEmpForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'roll/index.html')

def all_emp(request):
    emps=Employee.objects.all()
    return render(request,'roll/all_emp.html',{'emps':emps})

def add_emp(request):
    if request.method=='POST':
        fm=EmployeeForm(request.POST)
        if fm.is_valid():
            fm.save()
        messages.success(request, 'Add Employeee Successfullay')
    else:
        fm=EmployeeForm()
    return render(request,'roll/add_emp.html',{'form':fm})


def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            messages.success(request, 'Removed Employee Succesfully')
        except:
            return HttpResponse("Please Enter a Valid Emp Id")

    emps=Employee.objects.all()
    return render(request,'roll/remove_emp.html',{'emps':emps})



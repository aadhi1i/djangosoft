from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
# Create your views here.

def home(request):
    data  = Employee.objects.all()
    if request.method == 'POST':
        search = request.POST.get('Search')
        data1 = Employee.objects.filter(Q(Name__icontains=search))
        return render(request,'home.html',{'value':data1})
    return render(request,'home.html',{'value':data})



def create(requst):
    if requst.method == 'POST':
        name = requst.POST.get('name')
        department = requst.POST.get('department')
        designation = requst.POST.get('designation')
        date = requst.POST.get('date')
        salary = requst.POST.get('salary')
        image = requst.FILES.get('image')

        data = Employee()
        data.Name = name
        data.Department = department
        data.Designation = designation
        data.Start_date = date
        data.Salary = salary
        data.Photo = image
        data.save()
        return redirect('home')
    return render(requst,'create_employee.html')

def delete(request,id):
    dlt = Employee.objects.get(id=id)
    dlt.delete()
    return redirect('home')

def update(requst,id):
    data = Employee.objects.get(id=id)
    if requst.method == "POST":
        name = requst.POST.get('name')
        email = requst.POST.get('email')
        department = requst.POST.get('department')
        designation = requst.POST.get('designation')
        date = requst.POST.get('date')
        salary = requst.POST.get('salary')
        image = requst.FILES.get('image')

        data.Name = name
        data.Email = email
        data.Department = department
        data.Designation = designation
        data.Start_date = date
        data.Salary = salary
        if image:
         data.Photo = image
        data.save()
        return redirect('home')
    return render(requst,'update_employee',{'value':data})





        

    
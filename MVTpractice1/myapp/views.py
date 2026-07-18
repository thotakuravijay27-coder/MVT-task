from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Student
from myapp.forms import StudentForm
# Create your views here.

def addstudent(request):
    sform = StudentForm()
    if request.method=='POST':
        sform=StudentForm(request.POST)
        if sform.is_valid():
            sform.save(commit=True)
            return redirect("/")
    return render(request,'myapp/add.html',{'form':sform})

def getstudents(request):
    students = Student.objects.all()
    return render(request,'myapp/students.html',{'stuList':students})

def getstudent(request,id):
    stu = get_object_or_404(Student,StudentId=id)
    return render(request,'myapp/find.html',{'student':stu})

def deletestudent(request,id):
    stu = get_object_or_404(Student,StudentId=id)
    if request.method=='POST':
        stu.delete()
        return redirect('/')
    return render(request,'myapp/delete.html',{'student':stu})

def editstudent(request,id):
    stu = get_object_or_404(Student,StudentId=id)
    sform =StudentForm(instance=stu)
    if request.method=='POST':
        sform = StudentForm(request.POST,instance=stu)
        sform.save()
        return redirect("/")
    return render(request,'myapp/edit.html',{'form':sform})
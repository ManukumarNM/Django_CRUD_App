from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentsForm
from .models import Students
from django.contrib import messages 

def index(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Students Information Saved Successfully")
            return redirect("display")
            # students = Students.objects.all()
            # return render(request, 'display.html', {'students': students })
    else:
        form = StudentsForm()
    return render(request, 'index.html',{'form': form})

def display(request):
    students = Students.objects.all()
    return render(request,'display.html',{'students': students})

def edit(request, id):
    students = Students.objects.get(id=id)
    return render(request, 'edit.html',{'students':students})

def update(request, id):
    students = Students.objects.get(id=id)
    # model = Students
    form = StudentsForm(request.POST, instance=students)
    print("Hellooooooooooo")
    if form.is_valid():
        print("HIIIIIIIIIIIIIIIIIIIII")
        form.save()
        return redirect("display")
    return render(request,'edit.html',{'students': students})

def delete(request, id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect("display")



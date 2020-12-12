
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import forms, models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    mform=forms.FormClass()
    form=forms.FormClass()

    if request.method == 'POST':
        form = forms.FormClass(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # address = form.cleaned_data['address']
            # phone_number = form.cleaned_data['phone_number']
            # department = form.cleaned_data['department']
            # teacher_name = form.cleaned_data['teacher_name']
            # aggregate_percentage = form.cleaned_data['aggregate_percentage']
            # project_details = form.cleaned_data['project_details']
            # publication_details = form.cleaned_data['publication_details']
            # eca_details = form.cleaned_data['eca_details']
            # university_to_address = form.cleaned_data['university_to_address']
            # deadline = form.cleaned_data['deadline']
            # print(name, email, address, phone_number, department, teacher_name, aggregate_percentage, project_details,
            #       publication_details, eca_details, university_to_address)
            form.save()
            form=mform
    return render(request, 'studentform.html', {'forms': form})

def loginPage(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('teacher')
        else:
            return render(request, 'login.html')
    return render(request,'login.html')
    


@login_required(login_url='login')
def teacher(request, dept='All'):
    mstudent = models.Requests.object.all()
    print(request.user)
    context = {
        "mstudent":mstudent
    }
    return render(request, 'teacher.html', context)
    

def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def returnLetter(request):
    if(request.is_ajax):
        id=int(request.GET.get('id'))
        student=models.Requests.object.get(id=id)
        context={
            'name': student.name,
            'department': student.department,
            'email': student.email,
            'deadline': student.deadline
        }
        return JsonResponse(context)


def success(request):
    return HttpResponse("<h1>success</h1>")


def test(request):
    return render(request, 'datepicker.html', {})


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
            # name = forms.cleaned_data['name']
            # email = forms.cleaned_data['email']
            # address = forms.cleaned_data['address']
            # phone_number = forms.cleaned_data['phone_number']
            # department = forms.cleaned_data['department']
            # teacher_name = forms.cleaned_data['teacher_name']
            # aggregate_percentage = forms.cleaned_data['aggregate_percentage']
            # project_details = forms.cleaned_data['project_details']
            # publication_details = forms.cleaned_data['publication_details']
            # eca_details = forms.cleaned_data['eca_details']
            # university_to_address = forms.cleaned_data['university_to_address']
            # # deadline = forms.cleaned_data['deadline']
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
    return render(request, 'login.html')

@login_required(login_url='login')
def teacher(request, dept='All'):
    print(dept)
    students=models.student_data.object.all()
    department=models.department.object.all()
    context={
        'students':students,
        'department':department
    }
    return render(request, 'teacher.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def generate(request):
    if(request.is_ajax):
        id=int(request.GET.get('id'))
        student=models.student_data.object.get(id=id)
        context={
            'first_name': student.first_name,
            'last_name': student.last_name,
            }

def success(request):
    return HttpResponse("<h1>success</h1>")

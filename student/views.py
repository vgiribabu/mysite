
# Create your views here.
from django.shortcuts import render
from .models import StudentApp, StudentReg, Staff, Department
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User





def index_view(request):
    return render(request, 'student/index.html')


def application(request):
    if request.method == 'POST':
        StudentApp.objects.create(
            Student_name=request.POST['Student_name'],
            email=request.POST['email'],
            ssc_memo=request.FILES['ssc-memo'],
            inter_memo=request.FILES['inter-memo']
        )
        return HttpResponseRedirect(reverse('student:index'))
    return render(request, 'student/application.html')


def student_registration(request):
    if request.method == "POST":
        email = request.POST['student-email']
        stu = StudentApp.objects.get(email=email, is_verified=True)
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['student-email'],
            password=request.POST['password'],
        )
        dept = Department.objects.get(department_name=request.POST['dept'])
        if stu.email == user.email:
            StudentReg.objects.create(
                student_apps=stu,
                student_name=request.POST['student-name'],
                student_email=request.POST['student-email'],
                student_father_name=request.POST['student-father'],
                student_mother_name=request.POST['student-mother'],
                student_mobile=request.POST['student-mobile'],
                student_profile_photo=request.FILES['student-profile'],
                department=dept,
                user=user,
            )
        return HttpResponseRedirect(reverse('student:index'))
    return render(request, 'student/student_registration.html')


def staff_registration(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['staff-email'],
            password=request.POST['password'],
        )
        dep = Department.objects.get(department_name=request.POST['dep'])
        Staff.objects.create(
            staff_name=request.POST['staff-name'],
            staff_email=request.POST['staff-email'],
            staff_father_name=request.POST['staff-father'],
            staff_mother_name=request.POST['staff-mother'],
            staff_profile_photo=request.FILES['staff-Profile'],
            staff_mobile=request.POST['staff-mobile'],
            department=dep,
            user=user,
        )
        return HttpResponseRedirect(reverse('student:index'))
    return render(request, 'student/staff_registration.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'studentreg'):
                return HttpResponseRedirect(reverse('student:details'))
            elif hasattr(user, 'staff'):
                return HttpResponseRedirect(reverse('student:details'))
        else:
            return render(request, 'student/login.html', {'error_message': "Invalid Credentials given"})
    return render(request, 'student/login.html')


def details(request):
    user = request.user
    if hasattr(user, 'studentreg'):
        return render(request, 'student/student_details.html', {'stu_det': request.user.studentreg})
    else:
        return render(request, 'student/staff_details.html', {'sta_det': request.user.staff})


def student_staff_list(request):
    dep = request.user.studentreg.department
    st_list = Staff.objects.filter(department=dep)
    return render(request, 'student/student_staff_list.html', {'st_list': st_list})
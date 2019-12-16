from django.urls import path
from . import views
from .api import StudentAppView, StudentRegView, StaffView
from rest_framework .authtoken.views import obtain_auth_token

app_name = 'student'
urlpatterns = [
    # path('', views.index_view, name='index'),
    # path('application/', views.application, name='application'),
    # path('student_registration/', views.student_registration, name='student-registration'),
    # path('staff_registration/', views.staff_registration, name='staff-registration'),
    # path('login/', views.login_view, name='login'),
    # path('details/', views.details, name='details'),
    # path('student_staff_list/', views.student_staff_list, name='student-staff-list'),
      path('Student_app/', StudentAppView.as_view()),
      path('Student_reg/', StudentRegView.as_view()),
      path('Staff/', StaffView.as_view()),
      # path('login/', obtain_auth_token),
]
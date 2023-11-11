from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage),
    path('student', views.Student_login),
    path('sregister', views.Student_registration),
    path('dashboard/<int:id>', views.stu_dashboard),
    path('tdashboard/<int:id>', views.teac_dashboard),
    path('teacher', views.teacher_login),
    path('tregister', views.teacher_registration),
    path('tdashboard/tassignment', views.teacher_assignemt),
    path('dashboard/sassignment', views.student_assignment)
]
   
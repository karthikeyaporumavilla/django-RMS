from django.urls import path

from . import views
from .views import delete_student

urlpatterns = [
    path("Homepage", views.Homepage, name="Homepage"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("checkregistration", views.checkregistration, name="checkregistration"),
    path("checkfacultylogin", views.checkfacultylogin, name="faculty_home"),
    path("checkstudentlogin", views.checkstudentlogin, name="checkstudentlogin"),
    path("facultyRegistration", views.facultyRegistration, name="facultyRegistration"),
    path("viewfaculty", views.viewfaculty, name="viewfaculty"),
    path("viewstudent", views.viewstudent, name="viewstudent"),
    path("studentRegistration", views.studentRegistration, name="studentRegistration"),
    path('faculty_home', views.faculty_home, name="faculty_home"),
    path('post_marks', views.post_marks, name="post_marks"),
    path('course', views.course, name='course'),
    path('viewcourses', views.view_courses, name='view_courses'),
    path('logout', views.logout_view, name='logout'),
    path('exam-results', views.view_exam_results, name='exam_results'),
    path('admin_exam_results', views.admin_view_exam_results, name='admin_exam_results'),
    path('update_faculty/', views.update_faculty, name='update_faculty'),
    path('delete_faculty/', views.delete_faculty, name='delete_faculty'),
    #path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('delete_student/',views.delete_student,name='delete_student'),
]

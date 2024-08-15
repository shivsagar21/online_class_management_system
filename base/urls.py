from django.urls import path
from . import views

urlpatterns=[
    path("",views.LandingPage,name="landingpage"),
    path("check/",views.check,name="check"),

    #User rooms
    path("teacher_room/",views.teacher_room,name="teacher-room"),
    path("student_room/",views.student_room,name="student-room"),


    #login-register users
    path("login_student/",views.StudentLogin,name="student-login"),
    path("register_student/",views.StudentRegister,name="student-register"),
    path("register_teacher/",views.TeacherRegister,name="teacher-register"),
    path("login_teacher/",views.TeacherLogin,name="teacher-login"),
    path('delete_room/<int:room_id>/', views.delete_room, name='delete-room'),
    #functionality 
    path("join_room/",views.Join,name="join"),
    path("snotice_box/",views.student_notice,name="snotice_box"),
    path("sactivity/",views.sactivity,name="sactivity"),
    path("tactivity/",views.tactivity,name="tactivity"),
    path("students/",views.students,name="students"),
    path("tallstudents/",views.tallstudents,name="tallstudents"),
    path("professors/",views.professors,name="professors"),
    path("sroom/<str:pk>/rstudents/",views.rstudents,name="rstudents"),
    path("troom/<str:pk>/trstudents/",views.trstudents,name="trstudents"),

    path('sroom/<str:pk>/',views.sroom,name="sroom"),
    path('troom/<str:pk>/',views.troom,name='troom'),
    path('create_room/',views.create_room,name='create-room'),
     path('create_notice/',views.create_notice,name='create-notice'),
    path('noticebox/', views.noticebox, name='noticebox'),
    path('logout_student/',views.LogOutStudent,name="logout-student"),
    path('logout_teacher/',views.LogOutTeacher,name="logout-teacher"),

    #update / view profile
    path('studentProfile/',views.studentProfile,name='studentProfile'),
    path('ProfessorProfile/',views.ProfessorProfile,name='ProfessorProfile'),
    path('studentprofileupdate/',views.studentprofileupdate,name='studentprofileupdate'),
    path('Professorprofileupdate/',views.Professorprofileupdate,name='Professorprofileupdate'),


    #files

    path('troom/<str:pk>/files/',views.files,name='tfiles'),
    path('troom/<str:pk>/files/upload/',views.tuploadfiles,name='tuploadfiles'),
    path('download/file/<int:file_id>/', views.download_file_files, name='download_file_files'),
    path('sroom/<str:pk>/files',views.sfiles,name="sfiles"),

    #lectures
    path('troom/<str:pk>/lectures/',views.lectures,name='tlectures'),
    path('troom/<str:pk>/lectures/upload/',views.tuploadlectures,name='tuploadlectures'),
    path('download/lecture/<int:file_id>/', views.download_file_lectures, name='download_file_lectures'),
    path('sroom/<str:pk>/lectures',views.slectures,name="slectures"),

    #assignment
    path('troom/<str:pk>/tassignments',views.tassignments,name='tassignments'),
    path('troom/<str:pk>/tassignments/upload',views.tuploadassignments,name='tuploadassignments'),
    path('download/tassignments/<int:file_id>/', views.download_file_tassignments, name='download_file_tassignments'),
    path('sroom/<str:pk>/sassignments/',views.sassignments,name="sassignments"),
    path('sroom/<str:pk>/sassignments/submission',views.submission,name="submission"),
    path('troom/<str:pk>/assignmentsubmission',views.tasubmission,name="tasubmission"),
    path('download/submissions/<int:file_id>/', views.download_file_submissions, name='download_file_submissions'),

    #tests
    path('troom/<str:pk>/ttest',views.ttest,name='ttest'),
    path('troom/<str:pk>/ttest/upload',views.tuploadtest,name='tuploadtest'),
    path('download/ttest/<int:file_id>/', views.download_file_ttest, name='download_file_ttest'),
    path('sroom/<str:pk>/stest/',views.stest,name="stest"),
    path('sroom/<str:pk>/stest/tsubmission',views.tsubmission,name="tsubmission"),
    path('troom/<str:pk>/testsubmission',views.ttsubmission,name="ttsubmission"),
    path('download/tsubmissions/<int:file_id>/', views.download_file_tsubmissions, name='download_file_tsubmissions'),









    #live meet
    path('troom/<str:pk>/createmeet',views.create_meeting,name='create_meeting'),
    path('tcalendar/',views.tcalendar,name="tcalendar"),
    path('scalendar/',views.scalendar,name="scalendar"),


]
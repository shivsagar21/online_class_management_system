from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User,Notice ,Teacher,Student,Room,Message,Files,Lectures,Tassignments,Meeting,Submissions,Ttest,Tsubmissions
from base import models
from .forms import StudentRegisterForm,TeacherRegisterForm,StudentUpdateForm,TeacherUpdateForm,UserForm,CreateRoomForm,FileForm,LectureForm,TassignmentForm,SubmissionForm,TtestForm,tsubmissionForm,CreateNoticeForm
from .forms import MeetingForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging


@login_required(login_url='check')
def portal(request):
    return render(request,'base/portal.html',{})

@login_required(login_url='check')
def student_room(request):

    Student_User=get_object_or_404(Student,user=request.user)
    rooms=Student_User.rooms.all

    context={'rooms':rooms}
    return render(request,'base/student_room.html',context)

@login_required(login_url='check')
def teacher_room(request):
    # Teacher_User=Teacher.objects.get(user=request.user)
    Teacher_User=get_object_or_404(Teacher, user=request.user)
    rooms=Teacher_User.rooms.all
    context={'rooms':rooms}
    return render(request,'base/teacher_room.html',context)


def LandingPage(request):
    return render(request,'base/landingpage.html',{})

def check(request):
    return render(request,'base/check.html',{})

def StudentLogin(request):
    # if request.user.is_authenticated:
    #     return redirect('portal')
    
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     user=User.objects.get(email=email)
        # except:
        #     messages.error(request, 'User does not exist!!')
        
        # user = authenticate(request, email=email, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect('portal')
        # else:
        #     messages.error(request, 'Username OR password does not exit')

        if user := authenticate(username=username, password=password):
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('student-room')

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('student-login')
    return render(request,'base/login_student.html',{})

#TeacherLogin

def LogOutStudent(request):
    logout(request)
    return redirect('landingpage')

def LogOutTeacher(request):
    logout(request)
    return redirect('landingpage')


def StudentRegister(request):
    user_type="student"
    # form = StudentRegisterForm()

    if request.method == 'POST':
        student_form = StudentRegisterForm(request.POST)
        user_form=UserForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
                messages.error(request,'Successfully Registered')
            # if user_form.DoesNotExist:
                user=user_form.save(commit=False)
                user.is_student=True
                user.save()

                profile=student_form.save(commit=False)
                profile.user=user
                profile.save()
                return redirect('student-room')
            # else:
                messages.error(request,'User already exists with this mailID')
        else:
            messages.error(request,'An error occured during Student Registration')
    else:
        user_form=UserForm()
        student_form=StudentRegisterForm()

    context={'user_form':user_form,'student_form':student_form}

    return render(request,'base/student_register.html',context)

def TeacherRegister(request):
    user_type="student"
    # form = StudentRegisterForm()

    if request.method == 'POST':
        Teacher_form = TeacherRegisterForm(request.POST)
        user_form=UserForm(request.POST)
        if user_form.is_valid() and Teacher_form.is_valid():
            # if user_form.DoesNotExist:
                user=user_form.save(commit=False)
                user.is_teacher=True
                user.save()

                profile=Teacher_form.save(commit=False)
                profile.user=user
                profile.save()
                return redirect('teacher-login')
            # else:
                messages.error(request,'User already exists with this mailID')
        else:
            messages.error(request,'An error occured during Teacher Registration')
    else:
        user_form=UserForm()
        Teacher_form=TeacherRegisterForm()

    context={'user_form':user_form,'teacher_form':Teacher_form}

    return render(request,'base/teacher_register.html',context)




def TeacherLogin(request):
    # if request.user.is_authenticated:
    #     return redirect('portal')
    
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     user=User.objects.get(email=email)
        # except:
        #     messages.error(request, 'User does not exist!!')
        
        # user = authenticate(request, email=email, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect('portal')
        # else:
        #     messages.error(request, 'Username OR password does not exit')

        if user := authenticate(username=username, password=password):
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('teacher-room')

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('teacher-login')
    return render(request,'base/login_teacher.html',{})




def create_room(request):
    form=CreateRoomForm()
    # Teacher_User=request.user.Teacher
    Teacher_User=get_object_or_404(Teacher, user=request.user)

    if request.method == 'POST':

        new_room=Room.objects.create(
            avatar=request.POST.get('avatar'),
            course_id=request.POST.get('course_id'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            room_code=request.POST.get('room_code'),
            # room=request.POST.get('room_id'),
            teacher=Teacher_User.name,
        )
        Teacher_User.rooms.add(new_room)
        return redirect('teacher-room')

    context={'form':form}

    return render(request, 'base/create_room.html',context)

def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    room.delete()
    return redirect('teacher-room')

def create_notice(request):
    form=CreateNoticeForm()
    # Teacher_User=request.user.Teacher
    Teacher_User=get_object_or_404(Teacher, user=request.user)

    if request.method == 'POST':

        new_notice=Notice.objects.create(
           
            description=request.POST.get('description'),
            # teacher=Teacher_User.name
            # room=request.POST.get('room_id'),

        )
        Teacher_User.notices.add(new_notice)
        return redirect('noticebox')

    context={'form':form}

    return render(request, 'base/create_notice.html',context)

def noticebox(request):
    # Teacher_User=Teacher.objects.get(user=request.user)
    Teacher_User=get_object_or_404(Teacher, user=request.user)
    notices=Teacher_User.notices.all
    context={'notices':notices}
    return render(request,'base/noticebox.html',context)

@csrf_protect
def Join(request):

    Student_User=get_object_or_404(Student, user=request.user)

    rooms=Room.objects.all()

    if request.method=='POST':
        room_id=request.POST.get('room_id')
        code=request.POST.get('code')
        room=Room.objects.get(id=room_id)
        print('checkingg...')
        if (code==room.room_code):
            messages.error(request,"Class Succesfully Joined")
            Student_User.rooms.add(room)
        
        else:
            messages.error(request,"Code don't match !!!")
 
    context={'rooms':rooms}
    return render(request,'base/join_room.html',context)

def student_notice(request):
    
    Student_User=get_object_or_404(Student, user=request.user)

    notices=Notice.objects.all()

    
    context={'notices':notices}
    return render(request,'base/snotice_box.html',context)

def firstword(a):
    p=a.split(" ")
    if p.size()>1:
        res=p[0][0].upper()+p[1][0].upper()
    else:
        res=p[0][0].upper()

    return res

def sroom(request ,pk):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all()
    participants=Student.objects.filter(rooms__id=pk)

    if request.method=='POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        return redirect('sroom',pk=room.id)
    
    context={'room':room,'room_messages':room_messages,'participants':participants}

    return render(request,'base/sroom.html',context)


def troom(request ,pk):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all()

    if request.method =='POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        return redirect('troom',pk=room.id)
    
    context={'room':room,'room_messages':room_messages}

    return render(request,'base/troom.html',context)

@login_required(login_url='check')
def sactivity(request):
    messages=Message.objects.filter(user=request.user)

    context={'messages':messages}

    return render(request,'base/sactivity.html',context)

def tactivity(request):
    messages=Message.objects.filter(user=request.user)

    context={'messages':messages}

    return render(request,'base/tactivity.html',context)


def students(request):
    students=Student.objects.all()

    context={'students':students}

    return render(request,'base/students.html',context)

def tallstudents(request):
    students=Student.objects.all()

    context={'students':students}

    return render(request,'base/tallstudents.html',context)

def professors(request):
    professors=Teacher.objects.all()
    context={'professors':professors}

    return render(request,'base/professors.html',context)

def rstudents(request, pk):
    room=Room.objects.get(id=pk)

    students=Student.objects.filter(rooms__id=pk)

    context={'room':room,'students':students}

    return render(request,'base/rstudents.html',context)


def trstudents(request,pk):
    room=Room.objects.get(id=pk)

    students=Student.objects.filter(rooms__id=pk)

    context={'room':room,'students':students}

    return render(request,'base/trstudents.html',context)



######Hunny code Update
def Professorprofileupdate(request):
    Teacher_User=get_object_or_404(Teacher,user=request.user)
    dict={}
    dict={'img':Teacher_User.avatar,'website':Teacher_User.websitelink,'name':Teacher_User.name,'Dep':Teacher_User.subject_name,'mail_id':Teacher_User.email,'bio':Teacher_User.bio,'phone':Teacher_User.phone}
    if request.method=="POST":
         
         
         image_=request.FILES.get('img')
         Teacher_User.name=request.POST.get('name')
         Teacher_User.websitelink=request.POST.get('website')
         if image_==None:
                Teacher_User.avatar=dict['img']
                
                
                
         else:
                Teacher_User.avatar=request.FILES.get('img')
                
                  
              
         Teacher_User.subject_name=request.POST.get('dep')
         Teacher_User.bio=request.POST.get('bio')
         
         Teacher_User.phone=request.POST.get('phone')
         Teacher_User.email=request.POST.get('email')
         Teacher_User.save()
         
       
     
    return render(request,'base/Professorprofileupdate.html',dict)


def studentProfile(request):
    Student_User=get_object_or_404(Student,user=request.user)
    dict={'img':Student_User.avatar,
          'roll_no':Student_User.roll_no,
          'name':Student_User.name,
          'Dep':Student_User.department,
          'mail_id':Student_User.email,
          'bio':Student_User.bio,
          'phone':Student_User.phone
          }
    return render(request,'base/studentProfile.html',dict)

def ProfessorProfile(request):
    Teacher_User=get_object_or_404(Teacher,user=request.user)
    
    dict={'img':Teacher_User.avatar,
          'website':Teacher_User.websitelink,
          'name':Teacher_User.name,
          'Dep':Teacher_User.subject_name,
          'mail_id':Teacher_User.email,
          'bio':Teacher_User.bio,
          'phone':Teacher_User.phone,
          
          }

    
    
    return render(request,'base/ProfessorProfile.html',dict)


def studentprofileupdate(request):
    Teacher_User=get_object_or_404(Student,user=request.user)
    dict={}
    dict={'img':Teacher_User.avatar,'roll_no':Teacher_User.roll_no,'name':Teacher_User.name,'mail_id':Teacher_User.email,'bio':Teacher_User.bio,'phone':Teacher_User.phone}
    if request.method=="POST":
         
         
         image_=request.FILES.get('img')
         Teacher_User.name=request.POST.get('name')
         Teacher_User.roll_no=request.POST.get('roll_no')
         if image_==None:
                Teacher_User.avatar=dict['img']
                
                
                
         else:
                Teacher_User.avatar=request.FILES.get('img')
                
                  
              
        #  Teacher_User.subject_name=request.POST.get('dep')
         Teacher_User.bio=request.POST.get('bio')
         
         Teacher_User.phone=request.POST.get('phone')
         Teacher_User.email=request.POST.get('email')
         Teacher_User.save()
       
     
    return render(request,'base/studentprofileupdate.html',dict)

#files
def files(request,pk):
    room=Room.objects.get(id=pk)

    files=Files.objects.filter(room__id=pk)
    context={'room':room,'files':files}
    return render(request,"base/tfiles.html",context)

def tuploadfiles(request,pk):
    room=Room.objects.get(id=pk)

    if request.method=='POST':
        form=FileForm(request.POST, request.FILES)
        if form.is_valid():
            file=form.save(commit=False)
            file.room=room
            file.uploaded_by=request.user.username
            file.save()

            return redirect('tfiles',pk=room.id)
        
    else:
        form=FileForm()
    context={'form':form,'room':room}   

    return render(request,'base/tuploadfiles.html',context)

def download_file_files(request, file_id):
    file = get_object_or_404(Files, id=file_id)
    response = HttpResponse(file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
    return response

def sfiles(request,pk):
    room=Room.objects.get(id=pk)
    files=Files.objects.filter(room__id=pk)

    context={'room':room,'files':files}
    return render(request,"base/sfiles.html",context)

#lectures
def download_file_lectures(request, file_id):
    file = get_object_or_404(Lectures, id=file_id)
    response = HttpResponse(file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
    return response


def lectures(request,pk):
    room=Room.objects.get(id=pk)

    lectures=Lectures.objects.filter(room__id=pk)
    context={'room':room,'lectures':lectures}
    return render(request,"base/tlectures.html",context)

def tuploadlectures(request,pk):
    room=Room.objects.get(id=pk)

    if request.method=='POST':
        form=LectureForm(request.POST, request.FILES)
        if form.is_valid():
            file=form.save(commit=False)
            file.room=room
            file.uploaded_by=request.user.username
            file.save()

            return redirect('tlectures',pk=room.id)
        
    else:
        form=FileForm()
    context={'form':form,'room':room}   

    return render(request,'base/tuploadlectures.html',context)


def slectures(request,pk):
    room=Room.objects.get(id=pk)
    lectures=Lectures.objects.filter(room__id=pk)

    context={'room':room,'lectures':lectures}
    return render(request,"base/slectures.html",context)


#Assignments

def tassignments(request,pk):
    room=Room.objects.get(id=pk)

    assignments=Tassignments.objects.filter(room__id=pk)
    context={'room':room,'assignments':assignments}

    return render(request,"base/tassignments.html",context)


def tuploadassignments(request,pk):
    room=Room.objects.get(id=pk)
    teacher=Teacher.objects.filter(rooms=room)

    if request.method=='POST':
        form=TassignmentForm(request.POST, request.FILES)
        if form.is_valid():
            file=form.save(commit=False)
            file.room=room
            file.teacher=teacher[0]
            file.save()

            return redirect('tassignments',pk=room.id)
    else:
        form=TassignmentForm()

    context={'form':form,'room':room}

    return render(request,'base/tuploadassignments.html',context)


def download_file_tassignments(request, file_id):
    file = get_object_or_404(Tassignments, id=file_id)
    response = HttpResponse(file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
    return response



def sassignments(request,pk):
    room=Room.objects.get(id=pk)
    assignments=Tassignments.objects.filter(room__id=pk)

    context={'room':room,'assignments':assignments}
    return render(request,"base/sassignments.html",context)

def submission(request,pk):
    room=Room.objects.get(id=pk)
    student=Student.objects.filter(user=request.user)

    if request.method=='POST':
        form=SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            file=form.save(commit=False)
            file.room=room
            file.student=student[0]
            messages.error(request,"Submitted Succesfully")
            file.save()

            return redirect('sassignments',pk=room.id)
    else:
        form=SubmissionForm()

    context={'form':form,'room':room}

    return render(request,'base/submission.html',context)

def tasubmission(request,pk):
    room=Room.objects.get(id=pk)
    submissions = Submissions.objects.filter(room_id=pk)

    context={'room':room,'submissions':submissions}
    return render(request,'base/tasubmission.html',context)

def download_file_submissions(request, file_id):
    file = get_object_or_404(Submissions, id=file_id)
    response = HttpResponse(file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
    return response


#test

def ttest(request,pk):
    room=Room.objects.get(id=pk)

    assignments=Ttest.objects.filter(room__id=pk)
    context={'room':room,'assignments':assignments}

    return render(request,"base/ttest.html",context)



def tuploadtest(request,pk):
    room=Room.objects.get(id=pk)
    teacher=Teacher.objects.filter(rooms=room)

    if request.method=='POST':
        form=TtestForm(request.POST, request.FILES)
        if form.is_valid():
            file=form.save(commit=False)
            file.room=room
            file.teacher=teacher[0]
            file.save()

            return redirect('ttest',pk=room.id)
    else:
        form=TtestForm()

    context={'form':form,'room':room}

    return render(request,'base/tuploadtest.html',context)


def download_file_ttest(request, file_id):
    file = get_object_or_404(Ttest, id=file_id)
    response = HttpResponse(file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
    return response


def stest(request,pk):
    room=Room.objects.get(id=pk)
    assignments=Ttest.objects.filter(room__id=pk)

    context={'room':room,'assignments':assignments}
    return render(request,"base/stest.html",context)



def tsubmission(request,pk):
    room=Room.objects.get(id=pk)
    student=Student.objects.filter(user=request.user)

    if request.method=='POST':
        form=tsubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            file=form.save(commit=False)
            file.room=room
            file.student=student[0]
            messages.error(request,"Submitted Succesfully")
            file.save()

            return redirect('stest',pk=room.id)
    else:
        form=tsubmissionForm()

    context={'form':form,'room':room}

    return render(request,'base/tsubmission.html',context)


def ttsubmission(request,pk):
    room=Room.objects.get(id=pk)
    submissions = Tsubmissions.objects.filter(room_id=pk)

    context={'room':room,'submissions':submissions}
    return render(request,'base/ttsubmission.html',context)


def download_file_tsubmissions(request, file_id):
    file = get_object_or_404(Tsubmissions, id=file_id)
    response = HttpResponse(file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
    return response




#live class
def create_meeting(request,pk):
    room=Room.objects.get(id=pk)
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.room=room
            meeting.save()
            return redirect('troom',pk=room.id)
    else:
        form = MeetingForm()
    return render(request, 'base/create_meeting.html', {'form': form,'room':room})


def tcalendar(request):
    teacher = Teacher.objects.get(user=request.user)
    meetings = Meeting.objects.filter(room__teacher=teacher)

    context={"teacher":teacher,'meetings':meetings}
    return render(request,"base/tcalendar.html",context)

def scalendar(request):
    student = Student.objects.get(user=request.user) 

    meetings = Meeting.objects.filter(room__in=student.rooms.all())

    context={"meetings":meetings,"student":student}

    return render(request,"base/scalendar.html",context)


from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Room,Notice, User,Student,Teacher,Files,Lectures,Tassignments,Meeting,Submissions,Ttest,Tsubmissions

from tempus_dominus.widgets import DateTimePicker




#for StudentLoginForm in html file itself
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']

#for registration
class StudentRegisterForm(ModelForm):
    class Meta():
        model = Student
        fields = ['name','email','roll_no','department']


class TeacherRegisterForm(ModelForm):
    class Meta():
        model = Teacher
        fields = ['name','email','subject_name']



class StudentUpdateForm(ModelForm):
    class Meta():
        model=Student
        fields='__all__'

class TeacherUpdateForm(ModelForm):
    class Meta():
        model=Teacher
        fields='__all__'


class CreateRoomForm(ModelForm):
    class Meta():
        model=Room
        fields=['course_id','name','description','room_code']


class FileForm(ModelForm):
    class Meta():
        model=Files
        fields=['name','description','file']

        widgets={
            'description': forms.Textarea(attrs={'rows':3}),
        }

class LectureForm(ModelForm):
    class Meta():
        model=Lectures
        fields=['name','description','file']

        widgets={
            'description': forms.Textarea(attrs={'rows':3}),
        }



class TassignmentForm(forms.ModelForm):
    class Meta:
        model = Tassignments
        fields = ['name', 'file', 'deadline']
        widgets = {
            'deadline': DateTimePicker(
                options={
                    'format': 'YYYY-MM-DD HH:mm', # specify the format of the date/time
                    'useCurrent': False, # do not use the current date/time as the default value
                }
            )
        }


class TtestForm(forms.ModelForm):
    class Meta:
        model = Ttest
        fields = ['name', 'file', 'deadline']
        widgets = {
            'deadline': DateTimePicker(
                options={
                    'format': 'YYYY-MM-DD HH:mm', # specify the format of the date/time
                    'useCurrent': False, # do not use the current date/time as the default value
                }
            )
        }



class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('name','link', 'start_time', 'end_time')
        

class SubmissionForm(forms.ModelForm):
    class Meta:
        model=Submissions
        fields=('name','description','file')


class tsubmissionForm(forms.ModelForm):
    class Meta:
        model=Tsubmissions
        fields=('name','description','file')




class CreateNoticeForm(ModelForm):
    class Meta():
        model=Notice
        fields=['description']        
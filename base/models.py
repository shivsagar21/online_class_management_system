from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
import sched, time
import os

# class Room:
#     pass

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    
    # email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS=[]
    

    

class Room(models.Model):
    # host = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    course_id=models.CharField(max_length=100)
    teacher=models.CharField(max_length=100)
    name = models.CharField(max_length=200) #set it to host.subject_name during declaration by default
    description = models.TextField(null=True, blank=True)
    
    avatar = models.ImageField(null=True, default="avatar.svg")
    room_code=models.CharField(max_length=100)

    #test
    # assignments
    #lectures
    #files

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Notice(models.Model):
    # host = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    id = models.AutoField(primary_key=True)
    description = models.TextField(null=True, blank=True)
    # teacher=models.CharField(max_length=100,default=None)
    


    #test
    # assignments
    #lectures
    #files
  
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name




class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Student')
    roll_no = models.CharField(max_length=50, null=True)
    name=models.CharField(max_length=250)
    email = models.EmailField(null=False)
    department=models.CharField(max_length=250 ,null=True)
    rooms=models.ManyToManyField(Room,related_name="student_rooms",blank=True)
    bio = models.TextField(null=True)
    phone = models.IntegerField(null=True)
    notices=models.ManyToManyField(Notice,related_name="student_notices",blank=True)
    

    avatar = models.ImageField(null=True, default="avatar.svg")
    #something with reverse absolutr url not written

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['roll_no']



class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Teacher')
    name=models.CharField(max_length=250)
    subject_name = models.CharField(max_length=250,null=True)
    email = models.EmailField(null=False)
    rooms=models.ManyToManyField(Room,related_name="teacher_rooms",blank=True)
    bio = models.TextField(null=True)
    phone = models.IntegerField(null=True)
    websitelink=models.URLField(max_length=200,null=True)
    notices=models.ManyToManyField(Notice,related_name="teacher_notices",blank=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    #something with reverse absolutr url not writte

    def __str__(self):
        return self.name

    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return self.body[0:50]


class ClassRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(
        Room, related_name='classroom_rooms', blank=True)
    
    

# class Assignment(models.Model):

class Files(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    uploaded_by = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('download_file_files', args=[str(self.id)])
    

class Lectures(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    file = models.FileField(upload_to='lectures/')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    uploaded_by = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('download_file_lectures', args=[str(self.id)])



class Tassignments(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    upload_at=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField()
    file=models.FileField(upload_to='tassignments/')

    def get_absolute_url(self):
        return reverse('download_file_tassignments', args=[str(self.id)])


class Submissions(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    file=file=models.FileField(upload_to='submissions/')
    name=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=400, null=True)
    upload_at=models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('download_file_submissions', args=[str(self.id)])

    class Meta:
        ordering=['upload_at']

#test
class Ttest(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    upload_at=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField()
    file=models.FileField(upload_to='ttest/')

    def get_absolute_url(self):
        return reverse('download_file_ttest', args=[str(self.id)])

class Tsubmissions(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    file=file=models.FileField(upload_to='tsubmissions/')
    name=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=400, null=True)
    upload_at=models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('download_file_tsubmissions', args=[str(self.id)])

    class Meta:
        ordering=['upload_at']

    

class Meeting(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    name=models.CharField(max_length=400 ,null=True , default="default")
    link = models.CharField(max_length=400)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def delete_meeting(self):
        self.delete()

    # def schedule_deletion(self):
    #     s = sched.scheduler(time.time, time.sleep)

    #     end_time = timezone.localtime(self.end_time)
    #     delay = (end_time - timezone.localtime(timezone.now())).total_seconds()

    #     s.enter(delay, 1, self.delete_meeting)

    #     s.run()

    # def save(self, *args, **kwargs):
    #     super(Meeting, self).save(*args, **kwargs)
    #     self.schedule_deletion()

    def __str__(self):
        return self.link


    class Meta:
        ordering = ['start_time']

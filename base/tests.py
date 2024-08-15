from django.test import TestCase
from .models import User, Room, Student, Teacher,Message,Files,Lectures
from django.urls import reverse
from django.contrib.auth import get_user_model


class ModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='testuser1')
        self.user2 = User.objects.create(username='testuser2')
        self.room1 = Room.objects.create(course_id='CSC101', teacher='John Doe', name='Introduction to Computer Science', description='This course introduces students to the fundamentals of computer science.')
        self.room2 = Room.objects.create(course_id='MAT201', teacher='Jane Smith', name='Calculus I', description='This course covers differential calculus of functions of one variable.')
        self.student1 = Student.objects.create(user=self.user1, roll_no='001', name='Alice', email='alice@example.com', department='Computer Science', phone='1234567890')
        self.teacher1 = Teacher.objects.create(user=self.user2, name='John Doe', subject_name='Computer Science', email='jdoe@example.com', phone='1234567890')


    def test_user(self):
        self.assertEqual(self.user1.is_student, False)
        self.assertEqual(self.user1.is_teacher, False)

    def test_room(self):
        self.assertEqual(self.room1.course_id, 'CSC101')
        self.assertEqual(self.room1.teacher, 'John Doe')
        self.assertEqual(self.room1.name, 'Introduction to Computer Science')
        self.assertEqual(self.room1.description, 'This course introduces students to the fundamentals of computer science.')
        self.assertEqual(self.room1.room_code, '')

    def test_student(self):
        self.assertEqual(self.student1.roll_no, '001')
        self.assertEqual(self.student1.name, 'Alice')
        self.assertEqual(self.student1.email, 'alice@example.com')
        self.assertEqual(self.student1.department, 'Computer Science')
        self.assertEqual(self.student1.phone, '1234567890')

    def test_teacher(self):
        self.assertEqual(self.teacher1.name, 'John Doe')
        self.assertEqual(self.teacher1.subject_name, 'Computer Science')
        self.assertEqual(self.teacher1.email, 'jdoe@example.com')
        self.assertEqual(self.teacher1.phone, '1234567890')

class MessageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User = get_user_model()
        cls.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        cls.room = Room.objects.create(
            course_id='COMP101',
            teacher='Test Teacher',
            name='Test Room',
            description='Test Room Description',
            room_code='12345'
        )
        cls.message = Message.objects.create(
            user=cls.user,
            room=cls.room,
            body='Test Message'
        )

    def test_message_user_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')
    
    def test_message_room_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('room').verbose_name
        self.assertEqual(field_label, 'room')

    def test_message_body_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('body').verbose_name
        self.assertEqual(field_label, 'body')

    def test_message_updated_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('updated').verbose_name
        self.assertEqual(field_label, 'updated')

    def test_message_created_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('created').verbose_name
        self.assertEqual(field_label, 'created')

    def test_message_body_max_length(self):
        message = Message.objects.get(id=1)
        max_length = message._meta.get_field('body').max_length
        self.assertEqual(max_length, 1000)

    def test_message_ordering(self):
        messages = Message.objects.all()
        self.assertEqual(messages[0], self.message)

    def test_message_str_method(self):
        message = Message.objects.get(id=1)
        self.assertEqual(str(message), 'Test Message')

class FilesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create test room
        test_room = Room.objects.create(
            name='Test Room', course_id='101', teacher='Test Teacher')

        # Create test file
        test_file = Files.objects.create(
            room=test_room,
            file='test_file.txt',
            name='Test File',
            description='This is a test file',
            uploaded_by='Test User'
        )

    def test_name_max_length(self):
        file = Files.objects.get(id=1)
        max_length = file._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class LecturesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create test room
        test_room = Room.objects.create(
            name='Test Room', course_id='101', teacher='Test Teacher')

        # Create test lecture
        test_lecture = Lectures.objects.create(
            room=test_room,
            file='test_lecture.mp4',
            name='Test Lecture',
            description='This is a test lecture',
            uploaded_by='Test User'
        )

    def test_name_max_length(self):
        lecture = Lectures.objects.get(id=1)
        max_length = lecture._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    
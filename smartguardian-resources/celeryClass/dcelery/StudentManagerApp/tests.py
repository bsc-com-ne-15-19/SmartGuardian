from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Student, PhoneNumbers
from .serializers import StudentSerializer

class StudentListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.phone_number = PhoneNumbers.objects.create(phone_number='1234567890')
        self.student = Student.objects.create(student_id='1', phone_number=self.phone_number, primary_location='Location', first_name='First', last_name='Last', gender='Male')

    def test_student_list(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [StudentSerializer(self.student).data])

from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
# from rest_framework.permissions import IsAuthenticated

class ReactView(generics.ListCreateAPIView):
    """
    A view for handling React requests related to students.

    This view allows listing and creating student objects.

    Attributes:
        queryset (QuerySet): The queryset of all Student objects.
        serializer_class (Serializer): The serializer class for Student objects.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated]
    
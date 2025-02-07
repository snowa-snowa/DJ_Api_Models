from rest_framework import viewsets,  filters
from .models import Book, Course, Student, Library, License, Driver
from .serializers import BookSerializer, CourseSerializer, StudentSerializer, LibrarySerializer, LicenseSerializer, DriverSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'author', 'title']

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields  = ['title']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'title']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'name']


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'location', 'name']


class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'license_number', 'issued_at', 'driver']


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'name', 'age']

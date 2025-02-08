from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class License(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name="license")
    license_number = models.CharField(max_length=20, unique=True)
    issued_at = models.DateField()

    def __str__(self):
        return self.license_number



class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="books")
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, related_name="courses")

    def __str__(self):
        return self.title

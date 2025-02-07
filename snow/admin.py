from django.contrib import admin
from .models import Driver, License, Library, Book, Student, Course

admin.site.register(Driver)
admin.site.register(License)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Course)

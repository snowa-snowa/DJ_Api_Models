from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField

from .models import Driver, License, Library, Book, Student, Course

class DriverSerializer(serializers.ModelSerializer):

    license = serializers.HyperlinkedIdentityField(view_name='license-detail')

    # books = serializers.HyperlinkedIdentityField(view_name='book-detail')

    class Meta:
        model = Driver
        fields = ('id', 'name', 'age', 'license')


class LicenseSerializer(serializers.ModelSerializer):



    class Meta:
        model = License
        fields = ('id', 'license_number', 'issued_at')


class LibrarySerializer(serializers.ModelSerializer):

    # books = serializers.HyperlinkedIdentityField(view_name='book-detail')

    books = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    # books = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='book-detail')

    # books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # books = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Library
        fields = ('id', 'name', 'location', 'books')



class BookSerializer(serializers.ModelSerializer):



    class Meta:
        model = Book
        fields = ('id', 'library', 'title',  'author')


class StudentSerializer(serializers.ModelSerializer):
    # Specify for every singer a single song as identity field
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')

    # SlugRelatedField is like StringRelatedField
    # song = serializers.SlugRelatedField(many=True, read_only=True,
    #                                     slug_field='title')

    # When slug_field='duration', it will show duration of song
    # song = serializers.SlugRelatedField(many=True, read_only=True,
    #                                     slug_field='duration')

    # Create clickable links for songs using HyperlinkedRelatedField
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True,
    #                                            view_name='song-detail')

    # Show id of songs using PrimaryKeyRelatedField
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    """Add song field that has been defined in models.py in ForeignKey
                relationship. It will show songs (title) associated with the singers"""

    # song = serializers.StringRelatedField(many=True, read_only=True)

    """Add song field that has been defined in models.py in ForeignKey
            relationship. It will show songs associated with the singers"""

    courses = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    # courses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='course-detail')

    class Meta:
        model = Student
        fields = ('id', 'name', 'courses')


class CourseSerializer(serializers.ModelSerializer):

    students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='student-detail')

    class Meta:
        model = Course
        fields = ('id', 'title', 'students')

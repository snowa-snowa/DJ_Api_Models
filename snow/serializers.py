from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField
from .models import Driver, License, Library, Book, Student, Course


class DriverSerializer(serializers.ModelSerializer):

    # license = serializers.HyperlinkedIdentityField(view_name='license-detail')
    """показывает ссылку на объект. показывает ссылку на объект с тем же id что и у объекта связанного с ним моделя"""

    # license = serializers.SlugRelatedField(read_only=True, slug_field='license_number')
    """показывает выбранное поле объекта, но так как связь OneToOneField и у одного объекта этого моделя не может быть
       несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    license = serializers.StringRelatedField(read_only=True)
    """показывает то что возвращается в admin или (object id). но так как связь OneToOneField и у одного объекта этого 
    моделя не может быть несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    class Meta:
        model = Driver
        fields = ('id', 'name', 'age', 'license')


class LicenseSerializer(serializers.ModelSerializer):

    driver = serializers.HyperlinkedIdentityField(view_name='driver-detail')
    """показывает ссылку на объект. показывает ссылку на объект с тем же id что и у объекта связанного с ним моделя"""
    """Не обязательно чтобы переменная была связывающей переменной между моделями, нужно лишь название самого моделя"""

    # driver = serializers.SlugRelatedField(read_only=True, slug_field='name')
    """показывает выбранное поле объекта, но так как связь OneToOneField и у одного объекта этого моделя не может быть
       несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    # driver = serializers.StringRelatedField(read_only=True)
    """показывает то что возвращается в admin или (object id). но так как связь OneToOneField и у одного объекта этого 
    моделя не может быть несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    class Meta:
        model = License
        fields = ('id', 'license_number', 'issued_at', 'driver')



class LibrarySerializer(serializers.ModelSerializer):

    # books = serializers.HyperlinkedIdentityField(view_name='book-detail')
    """можно использовать, но работать будет некорректно, так как HyperlinkedIdentityField предназначен для связи
       моделей OneToOneField. покажет ссылку объекта с тем же id что и у объекта связанного с ним моделя, даже если такого
       объекта не существует он все ровно покажет ссылку"""

    books = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    """показывает выбранное поле объекта"""

    # books = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='book-detail')
    """показывает ссылки на все объекты"""

    # books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """показывает id объектов"""

    # books = serializers.StringRelatedField(many=True, read_only=True)
    """показывает главное поле объекта, его имя, название"""

    class Meta:
        model = Library
        fields = ('id', 'name', 'location', 'books')


class BookSerializer(serializers.ModelSerializer):

    # library = serializers.SlugRelatedField(read_only=True, slug_field='name')
    """показывает выбранное поле объекта, но так как связь ForeignKey и у одного объекта этого моделя не может быть
       несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    # library = serializers.PrimaryKeyRelatedField(read_only=True)
    """показывает id объекта. но так как связь ForeignKey и у одного объекта этого моделя не может быть
       несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    library = serializers.StringRelatedField(read_only=True)
    """показывает главное поле объекта, его имя, название. но так как связь ForeignKey и у одного объекта этого моделя
       не может быть несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    class Meta:
        model = Book
        fields = ('id', 'library', 'title',  'author')



class StudentSerializer(serializers.ModelSerializer):

    # courses = serializers.HyperlinkedIdentityField(view_name='course-detail')
    """можно использовать, но работать будет некорректно, так как HyperlinkedIdentityField предназначен для связи
       моделей OneToOneField. покажет ссылку объекта с тем же id что и у объекта связанного с ним моделя, даже если такого
       объекта не существует он все ровно покажет ссылку"""

    courses = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    """показывает выбранное поле объекта. не показывает поля в которых может быть несколько объектов"""

    # courses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='course-detail')
    """показывает ссылки на все объекты"""

    # courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """показывает id объектов"""

    # courses = serializers.StringRelatedField(many=True, read_only=True)
    """показывает главное поле объекта, его имя, название"""

    class Meta:
        model = Student
        fields = ('id', 'name', 'courses')


class CourseSerializer(serializers.ModelSerializer):

    # students = serializers.HyperlinkedIdentityField(view_name='student-detail')
    """можно использовать, но работать будет некорректно, так как HyperlinkedIdentityField предназначен для связи
       моделей OneToOneField. покажет ссылку объекта с тем же id что и у объекта связанного с ним моделя, даже если такого
       объекта не существует он все ровно покажет ссылку"""

    # students = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    """показывает выбранное поле объекта"""

    # students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='student-detail')
    """показывает ссылки на все объекты"""

    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """показывает id объектов"""

    students = serializers.StringRelatedField(many=True, read_only=True)
    """показывает главное поле объекта, его имя, название"""

    class Meta:
        model = Course
        fields = ('id', 'title', 'students')

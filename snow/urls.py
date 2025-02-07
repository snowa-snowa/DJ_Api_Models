from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, DriverViewSet, LicenseViewSet, LibraryViewSet, StudentViewSet, CourseViewSet

router = DefaultRouter()

router.register(r'drivers', DriverViewSet)
router.register(r'licenses', LicenseViewSet)

router.register(r'books', BookViewSet, basename='book')
router.register(r'libraries', LibraryViewSet, basename='libraries')

router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]

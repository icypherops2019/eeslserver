"""
Urls for school app
"""
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from hbook.users.school.views import SchoolViewSet, StudentViewSet, TeacherViewSet, ClassGroupViewSet, SubjectViewSet, PeriodViewSet

SCHOOL_APP_ROUTER = DefaultRouter()

SCHOOL_APP_ROUTER.register('school', SchoolViewSet)
SCHOOL_APP_ROUTER.register('student', StudentViewSet)
SCHOOL_APP_ROUTER.register('teacher', TeacherViewSet)
SCHOOL_APP_ROUTER.register('classgroup', ClassGroupViewSet)
SCHOOL_APP_ROUTER.register('subject', SubjectViewSet)
SCHOOL_APP_ROUTER.register('period', PeriodViewSet)

urlpatterns=[url(r'^$', include(SCHOOL_APP_ROUTER.urls))]

from rest_framework.serializers import HyperlinkedModelSerializer
from hbook.users.school.models import School, Student, Teacher, ClassGroup, Subject, Period

class SchoolSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('url', 'owner', 'name', 'details', 'students', 'teachers', 'class_groups')

class StudentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'roll_number', 'name', 'school', 'auth', 'details', 'class_groups', 'periods_attended')

class TeacherSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'roll_number', 'name', 'school', 'auth', 'details', 'classes_incharged_with', 'periods')

class ClassGroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ClassGroup
        fields = ('url', 'students', 'name', 'school', 'teacher_incharge', 'details', 'subjects', 'periods')

class SubjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('url', 'name', 'time_alloted', 'max_consecutive_time', 'min_consecutive_time', 'class_groups_assigned', 'details', 'periods')

class PeriodSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = ('url', 'class_group', 'subject', 'teacher', 'from_time', 'to_time', 'students_present')
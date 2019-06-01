from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from hbook.users.school.models import *
from hbook.users.school.serilizers import *
from hbook.users.models import User2Serializer


def add_to_request(request, params):
    mutable = request.POST._mutable
    request.POST._mutable=True
    for x in params:
        request.POST[x]=params[x]
    request.POST._mutable = mutable
    return request

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @action(detail=False)
    def search(self, request):
        method = request.GET.get("method", "name")
        key = request.GET.get("key", "#")
        if key == "#":
            return Response({"status":"error", "message":"Bad Request"})
        schools=None
        if method == "name":
            # search by name for school
            schools = School.objects.filter(name__icontains=key)
        elif method == "id":
            # search by id and return the vaue
            schools = School.objects.filter(pk=key)
        return Response(SchoolSerializer(schools, many=True, context={'request':request}).data)
    
    def create(self, request):
        request = add_to_request(request, {'owner':User2Serializer(request.user.details, context={'request':request}).data['url']})
        return super(SchoolViewSet, self).create(request)
    

        


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassGroupViewSet(ModelViewSet):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class PeriodViewSet(ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

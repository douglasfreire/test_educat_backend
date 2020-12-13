from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from students.models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_fields = ('name',)

    filter_backends = (SearchFilter,)
    search_fields = ('name', 'id')


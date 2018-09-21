from django.shortcuts import render

# rest_frameowrk required modules
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees, Department
from .serializers import EmployeeSerializers, DepartmentSerializers

# Create your views here.


def home(request):

    return render(request, 'eze/index.html')


class employeeList(APIView):

    def get(self, request):
        employee = Employees.objects.all()
        serializer = EmployeeSerializers(employee, many=True)

        return Response(serializer.data)


class DepartmentList(APIView):

    def get(self, request):
        department = Department.objects.all()
        serializer = DepartmentSerializers(department, many=True)

        return Response(serializer.data)

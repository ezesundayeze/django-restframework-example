from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home, name="home"),
    path('api/employee', views.employeeList.as_view(), name="employee"),
    path('department/list', views.DepartmentList.as_view(), name="department"),
    path('admin/', admin.site.urls),
]

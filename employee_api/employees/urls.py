from django.urls import path
from .views import EmployeeListAPIView, EmployeeDeleteView, EmployeeRetrieveUpdateAPIView, EmployeeUpdateAPIView, \
    EmployeeRetrieveAPIView, EmployeeSearchAPIView, MyUserListCreateAPIView, MyUserRetrieveUpdateDestroyAPIView, \
    DepartmentListCreateAPIView, DepartmentRetrieveUpdateDestroyAPIView
from .views import EmployeeCreateAPIView

urlpatterns = [
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/<int:pk>', EmployeeDeleteView.as_view(), name='employee-list'),
    path('employee', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('employeeUpdate/<int:pk>', EmployeeRetrieveUpdateAPIView.as_view(), name='employee-update'),
    path('employee-update/<int:pk>', EmployeeUpdateAPIView.as_view(), name='employee-update'),
    path('employee-get/<int:pk>', EmployeeRetrieveAPIView.as_view(), name='employee-get'),
    path('employees-name/', EmployeeSearchAPIView.as_view(), name='employee-search'),
    path('users/', MyUserListCreateAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', MyUserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('departments/', DepartmentListCreateAPIView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyAPIView.as_view(), name='department-detail'),
]

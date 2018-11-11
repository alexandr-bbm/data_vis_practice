from django.urls import path
from lab2.views import IndexPageView, OrdersPerDatePageView, EmployeesPerDeptPageView, AvgSalaryPerDeptPageView
from django.conf.urls import url

urlpatterns = {
    path('', IndexPageView.as_view()),
    url(r'^orders_per_date/$', OrdersPerDatePageView.as_view()),
    url(r'^employees_per_dept/$', EmployeesPerDeptPageView.as_view()),
    url(r'^avg_salary_per_dept/$', AvgSalaryPerDeptPageView.as_view()),
}

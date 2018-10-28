from django.urls import path
from django.conf.urls import url

from course_work.views import MapView, IndexPageView

urlpatterns = {
    path('', IndexPageView.as_view(), name='index'),
    url(r'^map/$', MapView.as_view()),
}

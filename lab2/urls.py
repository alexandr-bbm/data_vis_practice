from django.urls import path
from lab2.views import IndexPageView

urlpatterns = {
    path('', IndexPageView.as_view()),
}

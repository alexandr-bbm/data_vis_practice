from django.urls import path

from lab4.views import IndexPageView, t2m_filtered

urlpatterns = {
    path('', IndexPageView.as_view(), name='index'),
    path('t2m', t2m_filtered, name='t2m_filtered'),
}

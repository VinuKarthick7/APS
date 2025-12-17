from django.urls import path
from .views import FacultyDashboardView

urlpatterns = [
    path('faculty/dashboard/', FacultyDashboardView.as_view()),
]

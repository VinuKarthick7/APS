from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import CourseAssignment, TeachingProgress
from .serializers import CourseAssignmentSerializer, TeachingProgressSerializer

class FacultyDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        print("LOGGED IN USER:")
        print("ID:", user.id)
        print("UID:", user.uid)
        print("ROLE:", user.role)

        assignments = CourseAssignment.objects.filter(faculty=user)
        progress = TeachingProgress.objects.filter(faculty=user)

        print("ASSIGNMENTS COUNT:", assignments.count())
        print("PROGRESS COUNT:", progress.count())

        return Response({
            "assignments": [],
            "progress": []
        })

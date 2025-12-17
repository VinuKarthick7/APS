from rest_framework import serializers
from .models import CourseAssignment, TeachingProgress


class CourseAssignmentSerializer(serializers.ModelSerializer):
    course_code = serializers.CharField(source='course.code')
    course_name = serializers.CharField(source='course.name')
    class_name = serializers.CharField(source='assigned_class.name')

    class Meta:
        model = CourseAssignment
        fields = ('course_code', 'course_name', 'class_name')


class TeachingProgressSerializer(serializers.ModelSerializer):
    topic_title = serializers.CharField(source='topic.title')
    status = serializers.CharField()
    hours_completed = serializers.IntegerField()

    class Meta:
        model = TeachingProgress
        fields = ('topic_title', 'status', 'hours_completed')


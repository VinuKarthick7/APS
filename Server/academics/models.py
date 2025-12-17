from django.db import models
from accounts.models import User


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Class(models.Model):
    """
    Example: CSE-2A, CSE-3B
    """
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Year {self.year})"


class CourseAssignment(models.Model):
    """
    Maps: Course + Class + Faculty
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('course', 'assigned_class')

    def __str__(self):
        return f"{self.course.code} → {self.assigned_class.name}"
    
class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    outcome = models.TextField()
    total_hours = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course.code} - {self.title}"

class TeachingProgress(models.Model):

    class Status(models.TextChoices):
        NOT_UPLOADED = "NOT_UPLOADED"
        UPLOADED = "UPLOADED"
        DISAPPROVED = "DISAPPROVED"
        APPROVED = "APPROVED"
        HOURS_SUBMITTED = "HOURS_SUBMITTED"
        VERIFIED = "VERIFIED"

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    course_assignment = models.ForeignKey(
        CourseAssignment,
        on_delete=models.CASCADE
    )
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_UPLOADED
    )

    content_url = models.URLField(blank=True, null=True)
    hours_completed = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('topic', 'course_assignment')

    def __str__(self):
        return f"{self.topic.title} - {self.course_assignment.assigned_class.name}"


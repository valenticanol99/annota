from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# --------------------------- PROJECT ---------------------------
class Project(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(null=True, default=None)
    end_date = models.DateField(null=True, default=None)
    description = models.TextField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, default="Planning")
    scrum_master = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# --------------------------- STATUS OF A TYPE USER STORY ---------------------------
class TypeUserStoryStatus(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name


# --------------------------- TYPE OF USER STORY ---------------------------
class TypeUserStory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True
    )
    id_type_us_status = models.ForeignKey(TypeUserStoryStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# --------------------------- USER STORY ---------------------------
def validate_number(value):
    if value < 0 or value > 10:
        raise ValidationError("Value between 0 and 10")


class UserStory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id_type_us = models.ForeignKey(TypeUserStory, on_delete=models.CASCADE)
    id_type_us_status = models.ForeignKey(
        TypeUserStoryStatus, on_delete=models.CASCADE, blank=True, null=True
    )
    status = models.CharField(max_length=50, blank=True, null=True)
    id_status = models.IntegerField(blank=True, null=True)
    business_priority = models.IntegerField(
        blank=False, null=True, validators=[validate_number]
    )
    technical_priority = models.IntegerField(
        blank=False, null=True, validators=[validate_number]
    )
    priority = models.IntegerField(blank=True, null=True)
    estimated_hours = models.IntegerField(blank=True, null=True)
    real_hours = models.IntegerField(blank=True, null=True)
    ps = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

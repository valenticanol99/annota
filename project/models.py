from django.db import models
from django.contrib.auth.models import User

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

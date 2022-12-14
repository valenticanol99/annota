from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Project, TypeUserStoryStatus

# --------------------------- PROJECT ---------------------------
class ProjectForm(ModelForm):
    class Meta:

        model = Project
        start_date = forms.DateField(widget=forms.SelectDateWidget)
        end_date = forms.DateField(widget=forms.SelectDateWidget)

        fields = ["name", "description", "scrum_master"]

        labels = {
            "name": "Project Name",
            "description": "Project Description",
            "scrum_master": "Scrum Master",
        }

        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


# --------------------------- STATUS ---------------------------
class TypeUserStoryStatusForm(ModelForm):
    class Meta:
        model = TypeUserStoryStatus

        fields = ["name", "description"]

        labels = {
            "name": "Status Name",
            "description": "Status Description",
        }

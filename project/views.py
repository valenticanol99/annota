from django.shortcuts import render, redirect

from .models import Project
from .forms import ProjectForm

from datetime import datetime

# --------------------------- HOME ---------------------------
def home(request):
    projects = Project.objects.all()

    if request.method == "GET":
        if "search" in request.GET.keys():
            projects = projects.filter(name__iexact=request.GET["search"]).values()

    context = {"projects": projects}
    return render(request, "home.html", context)


# --------------------------- PROJECT ---------------------------
def create_project(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/home")

    context = {"form": form}

    return render(request, "create_project.html", context)


def project(request, id_project):
    project = Project.objects.get(id=id_project)

    context = {"project": project}
    return render(request, "project.html", context)


def start_project(request, id_project):
    project = Project.objects.get(id=id_project)

    if project.status == "Planning":
        project.status = "Initiated"
        project.start_date = datetime.now()
        project.save()

    context = {"project": project}
    return render(request, "project.html", context)


def cancel_project(request, id_project):
    project = Project.objects.get(id=id_project)

    if project.status not in ["Canceled", "Ended"]:
        project.status = "Canceled"
        project.end_date = datetime.now()
        project.save()

    context = {"project": project}
    return render(request, "project.html", context)


def end_project(request, id_project):
    project = Project.objects.get(id=id_project)
    if project.status not in ["Canceled", "Ended"]:
        project.status = "Ended"
        project.end_date = datetime.now()
        project.save()

    context = {"project": project}
    return render(request, "project.html", context)

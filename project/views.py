from django.shortcuts import render, redirect

from .models import Project, TypeUserStoryStatus
from .forms import ProjectForm, TypeUserStoryStatusForm

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


# --------------------------- TYPE USER STORY ---------------------------


def type_us(request, id_project):
    project = Project.objects.get(id=id_project)

    context = {"project": project}
    return render(request, "type_us.html", context)


# --------------------------- TYPE USER STORY STATUS ---------------------------
def type_us_status(request, id_project):
    project = Project.objects.get(id=id_project)
    status = TypeUserStoryStatus.objects.all().filter(id_project=id_project)

    context = {"project": project, "status": status}
    return render(request, "type_us_status.html", context)


def create_type_us_status(request, id_project):
    form = TypeUserStoryStatusForm()
    project = Project.objects.get(id=id_project)

    if request.method == "POST":
        form = TypeUserStoryStatusForm(request.POST)

        if form.is_valid():
            status = form.save()
            status.id_project = project
            status.save()

            return redirect("/type_us_status/" + str(id_project))

    context = {"form": form, "project": project}

    return render(request, "create_type_us_status.html", context)


def delete_type_us_status(request, id_project, id_type_us_status):
    status = TypeUserStoryStatus.objects.get(id=id_type_us_status)
    status.delete()

    return redirect("/type_us_status/" + str(id_project))


def edit_type_us_status(request, id_project, id_type_us_status):
    project = Project.objects.get(id=id_project)
    type = TypeUserStoryStatus.objects.get(id=id_type_us_status)
    form = TypeUserStoryStatusForm(instance=type)

    if request.method == "POST":
        form = TypeUserStoryStatusForm(request.POST, instance=type)
        if form.is_valid():
            form.save()

            return redirect("/type_us_status/" + str(id_project))

    context = {"form": form, "project": project}
    return render(request, "edit_type_us_status.html", context)

from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    # --------------------------- PROJECT ---------------------------
    path("home/create_project", views.create_project, name="create_project"),
    path("project/<int:id_project>/", views.project, name="project"),
    path("start_project/<int:id_project>", views.start_project, name="start_project"),
    path(
        "cancel_project/<int:id_project>", views.cancel_project, name="cancel_project"
    ),
    path("end_project/<int:id_project>", views.end_project, name="end_project"),
]

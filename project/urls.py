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
    # --------------------------- TYPE USER STORY ---------------------------
    path("type_us/<int:id_project>/", views.type_us, name="type_us"),
    # --------------------------- TYPE USER STORY STATUS ---------------------------
    path(
        "type_us_status/<int:id_project>/", views.type_us_status, name="type_us_status"
    ),
    path(
        "type_us_status/<int:id_project>/create_type_us_status",
        views.create_type_us_status,
        name="create_type_us_status",
    ),
    path(
        "type_us_status/<int:id_project>/delete_type_us_status/<int:id_type_us_status>",
        views.delete_type_us_status,
        name="delete_type_us_status",
    ),
    path(
        "type_us_status/<int:id_project>/edit_type_us_status/<int:id_type_us_status>",
        views.edit_type_us_status,
        name="edit_type_us_status",
    ),
]

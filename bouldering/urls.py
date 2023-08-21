from django.urls import path

from . import views

app_name = "bouldering"
urlpatterns = [
    path("", views.room, name="room"),
    path("<int:wall_id>/", views.wall_section, name="wall_section"),
    path("add/<int:route_id>/<int:user_id>", views.add_send, name="add_send"),
    path("remove/<int:route_id>/<int:user_id>", views.remove_send, name="remove_send"),
    path("update/<int:wall_id>", views.upload_image, name="upload_image")
]

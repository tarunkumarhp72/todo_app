
from django.urls import path
from note import views

urlpatterns = [
  
    path("", views.note, name="note"),
    path("update-note/<id>/", views.update_note, name="update-note"),
    path("delete-note/<id>/", views.delete_note, name="delete-note"),
]

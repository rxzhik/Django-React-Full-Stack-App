from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    # In Django URL patterns, the syntax <int:pk> is a path converter that captures 
    # part of the URL and passes it to the view as a keyword argument.
    # The captured value is used to look up the instance that the view operates on,
    # but you need to specify what you've named it in the lookup_field, by default
    # which is set to 'pk', so here we don't ned to mention it in the view, but if
    # it was lets say <int:id> then we would need to do: lookup_field = 'id', in the view.
    path("notes/delete/<int:pk>", views.NoteDelete.as_view(), name="delete-note")
]
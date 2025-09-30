from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path("notes/create/", views.create_note, name="create_note"),
    path("notes/update/", views.update_note, name="update_note"),

]

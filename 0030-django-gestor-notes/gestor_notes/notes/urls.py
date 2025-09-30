from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_note/', views.create_note, name='create_note'),
    path('note/<int:pk>/', views.note_details, name='note_details'),
    path("notes/<int:pk>/edit/", views.edit_note, name="edit_note")

]

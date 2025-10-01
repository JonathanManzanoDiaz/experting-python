from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/create_post', views.create_post, name='create_post'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete')
]

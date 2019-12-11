
from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit', views.post_edit, name='post_edit'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('<int:post_pk>/comments/new/', views.comment_new, name="comment_new"),
    path('<int:post_pk>/comments/<int:pk>/edit/', views.comment_edit, name="comment_edit"),
    path('<int:post_pk>/comments/<int:pk>/delete/', views.comment_delete, name="comment_delete"),
]

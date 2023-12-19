from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_polls),
    path("add/", views.add_post),
    path("<int:pk>/", views.post_details),
]
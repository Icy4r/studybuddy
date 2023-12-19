from django.urls import path
from . import views

# urls
urlpatterns = [
    path('<str:username>/', views.profile_view),
]
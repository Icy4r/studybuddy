from django.urls import path
from . import views

# urls
urlpatterns = [
    path('login/', views.login_view),
    path('createaccount/', views.create_account),
]
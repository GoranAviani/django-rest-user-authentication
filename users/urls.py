from django.urls import include, path
from . import views

urlpatterns = [
    path('all/', views.UserListView.as_view()),
]

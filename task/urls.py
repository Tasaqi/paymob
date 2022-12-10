
from django.urls import path
from .views import FirstView, SecondView
urlpatterns = [
    path("", FirstView.as_view(), name="first_view"),
    path("/second", SecondView.as_view(), name="second_view")
]

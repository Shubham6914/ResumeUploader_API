
from django.urls import path
from .views import ProfileView
urlpatterns = [
   path('resume/',ProfileView.as_view(), name="resume"),
   path('list/',ProfileView.as_view(), name="list"),
]
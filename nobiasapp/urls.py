from django.urls import path

from . import views
from .views import submitLink

urlpatterns = [
    # path("", views.index, name="index"),
    path('submitLink/', submitLink,name='submitLink'),
]
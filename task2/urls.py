from django.urls import path
from .views import Task2View

urlpatterns = [
    path('data/', Task2View.as_view(), name='data'),
]

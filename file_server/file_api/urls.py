from django.urls import path
from .views import get_file_content

urlpatterns = [
    path('data/', get_file_content, name='get_file_content'),
]

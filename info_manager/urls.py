from django.urls import path, include

from . views import info_manager_index


app_name="info_manager"

urlpatterns = [
    path('info', info_manager_index, name='info_manager_index'),
]

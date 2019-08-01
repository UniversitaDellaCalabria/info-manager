from django.urls import path, include

from . views import info_manager_index, info_page


app_name="info_manager"

urlpatterns = [
    path('info', info_manager_index, name='info_manager_index'),
    path('info_page/<slug:slug>/', info_page, name='info_page'),

]

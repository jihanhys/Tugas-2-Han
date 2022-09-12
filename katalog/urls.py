# TODO: Implement Routings Here
from django.urls import path
from katalog.views import show_catalog

app_name = "Katalog Jihan"

urlpatterns = [
    path('', show_catalog, name = 'show_catalog')
]
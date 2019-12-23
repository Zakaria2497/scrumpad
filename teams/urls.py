from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('create/', views.TeamCreate.as_view(), name='create')
]
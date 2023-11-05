from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('create/', views.poll_create, name='poll_create'),
    path('<int:poll_id>/vote/', views.poll_vote, name='poll_vote'),
]

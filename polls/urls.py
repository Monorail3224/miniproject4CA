from django.urls import path
from .views import PollListView, PollDetailView, PollCreateView, PollEditView
from . import views

app_name = 'polls'

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list'),
    path('<int:poll_id>/', PollDetailView.as_view(), name='poll_detail'),
    path('create/', PollCreateView.as_view(), name='poll_create'),
    path('<int:poll_id>/edit/', PollEditView.as_view(), name='poll_edit'),
]

from django.urls import path
from .views import PollListView, PollDetailView, PollCreateView, PollEditView, RegisterView
from django.contrib.auth import views as auth_views

app_name = 'polls'

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list'),
    path('<int:poll_id>/', PollDetailView.as_view(), name='poll_detail'),
    path('create/', PollCreateView.as_view(), name='poll_create'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Redirect to home page after logout
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset.html'), name='password_reset_complete'),
    
    # Registration URL
    path('register/', RegisterView.as_view(), name='register'),
]

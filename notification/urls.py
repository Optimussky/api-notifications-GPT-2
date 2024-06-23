from django.urls import path
from .views import LoginView, SendNotificationView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('send/', SendNotificationView.as_view(), name='send_notification'),
]
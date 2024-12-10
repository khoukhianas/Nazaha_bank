from django.urls import path
from .views import DashboardStats
from .views import SignUpView, SignInView, ValidateTokenView


urlpatterns = [
    path('api/dashboard-stats/', DashboardStats.as_view(), name='dashboard-stats'),
    path('signup/', SignUpView.as_view(), name='signup'),  # Route pour s'inscrire
    path('signin/', SignInView.as_view(), name='signin'),
]

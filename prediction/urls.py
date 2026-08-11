from django.urls import path
from.views import home, history, delete_history,register,dashboard
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
     path("", home),
     path("prediction-page/", views.prediction_page, name="prediction_page"),
     path("history/", views.history, name ="history"),
     path("history/<int:id>",delete_history),
     path("home/", views.home_page, name="home_page"),
     path("register/",views.register, name = "register"),
     path("login/",TokenObtainPairView.as_view(), name = "token_obtain_pair"),
     path("refresh/",TokenRefreshView.as_view(), name = "token_refresh"),
     path("dashboard/",views.dashboard, name ="dashboard"),
    path("auth/", views.auth_page, name="auth_page"),
     path("dashboard-page/", views.dashboard_page, name="dashboard_page")

]
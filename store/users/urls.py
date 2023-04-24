from django.urls import path

from .import views
from .views import SignUpView,SignInView

app_name = 'users'

urlpatterns = [
    path('login/', SignInView.as_view(),name='login'),
    path('register/',SignUpView.as_view(),name='register'),
]

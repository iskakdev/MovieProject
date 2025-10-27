from django.urls import path, include
from .views import (RegisterView, CustomLoginView,
                    LogoutView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),
]
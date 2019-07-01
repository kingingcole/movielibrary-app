from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import current_user, CreateUser, AllUsers, UpdateDetails, UpdatePassword

urlpatterns = [
    path('current_user/', current_user),
    path('signup/', CreateUser.as_view()),
    path('login/', obtain_jwt_token),
    path('users/', AllUsers.as_view()),
    path('user/<int:pk>/', UpdateDetails.as_view()),
    path('user/change_password/<int:pk>/', UpdatePassword.as_view())
]

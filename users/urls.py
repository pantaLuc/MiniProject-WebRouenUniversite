from knox import views as knox_views
from .views import DeleteUser, ListUser, LoginAPI, RegisterAPI, UserAPI, ChangePasswordView
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/', UserAPI.as_view(), name='user'),
    path('deleteuser', DeleteUser.as_view(({
        'delete':'delete',
    }))),
    path('listuser/' ,ListUser.as_view(),name='listUser'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
from django.urls import path
from . import views


urlpatterns = [
    #setting up url
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout"),
    
    path('dashboard', views.dashboard, name="dashboard"),
    path('add-record', views.add_record, name="add-record"),
    
    path('update-record/<int:pk>', views.update_record, name="update-record"),

    path('record/<int:pk>', views.one_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

    
]
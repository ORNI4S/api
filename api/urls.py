from django.urls import path
from . import views


urlpatterns = [
    path('' , views.ServerStatus.as_view() , name='server_status'), 
    path('userinfo/<str:fruitpass>' , views.UserInfo.as_view(), name='user_info') , 
    path('sender/<str:fruitpass>/<int:date>/<int:chat_id>/<int:second>' , views.Sender.as_view() , name='sender')
]


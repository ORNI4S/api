from django.urls import path
from . import views


urlpatterns = [
    path('' , views.ServerStatus.as_view() , name='server_status'), 
    path('userinfo/<str:fruitpass>' , views.UserInfo.as_view(), name='user_info') , 
    path('sender/<str:fruitpass>/<int:date>/<int:chat_id>/<int:second>' , views.Sender.as_view() , name='sender') , 
    path('kill/<int:pid>' , views.Killer.as_view() ,  name='kill_pid')
]




#667d340953f5bd85db91f06e2d9c4150
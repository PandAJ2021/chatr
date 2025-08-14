from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('room/<str:room_name>/', views.chat_room, name='real_time_chat'), 
    path('create-room/', views.CreateChatRoomView.as_view(), name='create_chat_room'),
    path('room/leave/<int:membership_id>/', views.LeaveChatRoomView.as_view(), name='leave_room'),
]
from .models import ChatMessage, ChatRoom, ChatRoomMembership
from accounts.models import User
from django.db import IntegrityError


def get_or_create_room(name, user:User):
    chat_room, created = ChatRoom.objects.get_or_create(name=name, defaults={'author':user})
    if created:
        try:
            ChatRoomMembership.objects.create(room=chat_room, user=user)
        except IntegrityError:
            pass
    return chat_room

def join_room(room:ChatRoom, user:User):
    ChatRoomMembership.objects.get_or_create(room=room, user=user)

def save_message(room:ChatRoom, user:User, content):
    return ChatMessage.objects.create(room=room, user=user, content=content)
    
def get_recent_messages(room:ChatRoom, limit=100):
    qs = (room.messages.filter(is_deleted=False).select_related('user').order_by('-timestamp')[:limit])
    return list(reversed(qs))
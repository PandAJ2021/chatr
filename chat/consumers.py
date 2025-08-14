import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .services import get_or_create_room, get_recent_messages, save_message, join_room
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def get_or_create_room(self, name, user ):
        return get_or_create_room(name, user)
    
    @database_sync_to_async
    def get_recent_messages(self, room):
        return get_recent_messages(room)
    
    @database_sync_to_async
    def join_room(self, room, user):
        return join_room(room, user)
    
    @database_sync_to_async
    def save_message(self, room, user, content):
        return save_message(room, user, content)

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope.get('user')

        if not (self.user and self.user.is_authenticated):
            await self.close(code=4001)
            return

        self.room = await self.get_or_create_room(self.room_name, self.user)
        await self.join_room(self.room, self.user)

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        recent_messages = await self.get_recent_messages(self.room)
        for message in recent_messages:
            await self.send(text_data=json.dumps({
                'type':'history',
                'user':message.user.username,
                'message':message.content,
                'timestamp':message.timestamp.isoformat()
            }))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name
            )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data.get('message','')
        if not content:
            return
        
        message = await self.save_message(self.room, self.user, content)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'user':message.user.username,
                'message':message.content,
                'timestamp':message.timestamp
            }
        )
    
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type':'chat',
            'user':event['user'],
            'message':event['message'],
            'timestamp':event['timestamp'].isoformat()
        }))
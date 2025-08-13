from django.contrib import admin
from .models import ChatMessage, ChatRoom, ChatRoomMembership


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'timestamp', 'updated',)
    list_filter = ('is_deleted',)
    search_fields = ('user', 'room',)


@admin.register(ChatRoom)
class CharRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at',)
    search_fields = ('name', 'author',)


@admin.register(ChatRoomMembership)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'joined_at',)
    search_fields = ('user', 'room',)
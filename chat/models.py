from django.db import models
from django.conf import settings


class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, 
        null=True, related_name='chat_rooms'
        )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ChatRoomMembership(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='memberships'
        )
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['room', 'user'], name='unique_user_room')
        ] 

    def __str__(self):
        return f'{self.user.username} joined in {self.room}'


class ChatMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:

        indexes = [
            models.Index(fields=['room', 'timestamp']),
        ]
        ordering = ['-timestamp']

    def __str__(self):
        return f'Message from {self.user.username} in {self.room}'
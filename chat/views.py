from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateChatForm
from .models import ChatRoomMembership, ChatRoom
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def chat_room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})


class CreateChatRoomView(LoginRequiredMixin, View):
    form_class = CreateChatForm
    template_name = 'chat/create_room.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return redirect('chat:real_time_chat', room_name=name)
        return render(request, self.template_name, {'form': form})


class LeaveChatRoomView(LoginRequiredMixin, View):

    def get(self, request, membership_id):
        membership = get_object_or_404(ChatRoomMembership, pk=membership_id, user=request.user)
        membership.delete()
        messages.success(request, 'You left the group.', 'success')
        return redirect('accounts:user_profile')


class ListChatRoomView(LoginRequiredMixin, View):

    def get(self, request):
        rooms = ChatRoom.objects.all()
        return render(request, 'chat/chat_rooms.html', {'rooms':rooms})


class DeleteChatRoomView(LoginRequiredMixin, View):

    def get(self, request, room_id):
        room = get_object_or_404(ChatRoom, pk=room_id, author=request.user)
        room.delete()
        messages.success(request, 'You delete the group.', 'success')
        return redirect('accounts:user_profile')
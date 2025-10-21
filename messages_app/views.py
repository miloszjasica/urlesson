from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser 
from .models import Message
from .forms import MessageForm
from django.db.models import Q
from django.http import JsonResponse
import json

@login_required
def conversation(request, user_id):
    other_user = get_object_or_404(CustomUser, id=user_id)
    user = request.user

    messages = Message.objects.filter(
        Q(sender=user, recipient=other_user) |
        Q(sender=other_user, recipient=user)
    ).order_by('timestamp')

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = user
            message.recipient = other_user
            message.save()
            return redirect('conversation', user_id=other_user.id)
    else:
        form = MessageForm()

    sent_to = Message.objects.filter(sender=user).values_list('recipient', flat=True)
    received_from = Message.objects.filter(recipient=user).values_list('sender', flat=True)
    user_ids = set(list(sent_to) + list(received_from))
    users = CustomUser.objects.filter(id__in=user_ids)

    return render(request, 'messages/conversation.html', {
        'other_user': other_user,
        'messages': messages,
        'form': form,
        'users': users
    })

@login_required
def conversation_json(request, user_id):
    other_user = get_object_or_404(CustomUser, id=user_id)
    user = request.user

    if request.method == "GET":
        messages = Message.objects.filter(
            Q(sender=user, recipient=other_user) |
            Q(sender=other_user, recipient=user)
        ).order_by('timestamp')

        data = [{
            'id': msg.id,
            'sender': msg.sender.email,
            'sender_id': msg.sender.id,
            'content': msg.content,
            'timestamp': msg.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        } for msg in messages]

        return JsonResponse({'messages': data})

    elif request.method == "POST":
        content = json.loads(request.body).get('content')
        if not content:
            return JsonResponse({'success': False, 'error': 'Empty message'})

        msg = Message.objects.create(sender=user, recipient=other_user, content=content)
        return JsonResponse({'success': True, 'message_id': msg.id})

    return JsonResponse({'success': False, 'error': 'Invalid method'})

from .models import Message
from accounts.models import CustomUser
from django.db.models import Q

def global_chat_context(request):
    if not request.user.is_authenticated:
        return {}

    user = request.user
    sent_to = Message.objects.filter(sender=user).values_list('recipient', flat=True)
    received_from = Message.objects.filter(recipient=user).values_list('sender', flat=True)
    user_ids = set(list(sent_to) + list(received_from))
    users = CustomUser.objects.filter(id__in=user_ids)
    all_users = CustomUser.objects.exclude(id=user.id)
    return {
        'users': users,
        'all_users': all_users
    }
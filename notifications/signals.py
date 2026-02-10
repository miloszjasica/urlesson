from django.db.models.signals import post_save
from django.dispatch import receiver
from urlesson.models import LessonRequest
from notifications.models import Notification

@receiver(post_save, sender=LessonRequest)
def lesson_request_notification(sender, instance, created, **kwargs):
    """
    Tworzy powiadomienia dla teacher/student w zależności od statusu lekcji.
    """
    try:
        if created:
            if instance.teacher:
                Notification.objects.create(
                    user=instance.teacher,
                    message=f"New lesson request #{instance.id} by {instance.student.get_full_name() or instance.student.email}."
                )
        else:
            # Zmiana statusu lekcji
            if instance.status == "rejected" and instance.student:
                Notification.objects.create(
                    user=instance.student,
                    message=f"Your lesson request #{instance.id} with {instance.teacher.get_full_name() or instance.teacher.email} has been rejected."
                )
            elif instance.status == "accepted" and instance.student:
                Notification.objects.create(
                    user=instance.student,
                    message=f"Your lesson request #{instance.id} with {instance.teacher.get_full_name() or instance.teacher.email} has been accepted."
                )
            elif instance.status == "canceled" and instance.teacher:
                Notification.objects.create(
                    user=instance.teacher,
                    message=f"The lesson request #{instance.id} with {instance.student.get_full_name() or instance.student.email} has been canceled."
                )
    except Exception as e:
        # Logowanie błędu zamiast crashu
        import logging
        logging.error(f"Error creating notification for LessonRequest {instance.id}: {e}")

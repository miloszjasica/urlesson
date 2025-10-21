from django.urls import path
from . import views

urlpatterns = [
    path('conversation_json/<int:user_id>/', views.conversation_json, name='conversation_json'),
]

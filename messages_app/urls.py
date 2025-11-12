from django.urls import path
from . import views

urlpatterns = [
    path('conversation/<int:user_id>/', views.conversation, name='conversation'),
    path('conversation_json/<int:user_id>/', views.conversation_json, name='conversation_json'),
]

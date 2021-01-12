from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('message_post', views.message_post),
    path('comment/<int:i_id>', views.comment),
    path('comment/<int:messages_id>/post', views.post_comment),
    path('comment/<int:messages_id>/delete', views.delete_message),
]
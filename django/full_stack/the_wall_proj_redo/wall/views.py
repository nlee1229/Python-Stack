from wall.models import PostMessage
from django.shortcuts import render, redirect
from main_app.models import User
from .models import *

def wall(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': logged_in_user,
        'messages': PostMessage.objects.all().order_by('-created_at'),
    }
    return render(request, 'wall.html', context)

def message_post(request):
    PostMessage.objects.create(
        content = request.POST['message'],
        user = User.objects.get(id=request.session['user_id']),
    )
    return redirect('/wall')

def comment(request, i_id):
    logged_in_user = User.objects.get(id=request.session['user_id'])

    context = {
        'user': logged_in_user,
        'messages': PostMessage.objects.get(id=i_id),
        'comments': Comment.objects.all(),
    }
    return render(request, 'msg_comm.html', context)

def post_comment(request, messages_id):
    Comment.objects.create(
        content = request.POST['comment'], #coming from form name in mess_com.html
        user = User.objects.get(id=request.session['user_id']),
        postmessage = PostMessage.objects.get(id=messages_id),
    )
    return redirect(f'/wall/comment/{messages_id}')

def delete_message(request, messages_id):
    post_delete = PostMessage.objects.get(id=messages_id)

    post_delete.delete()

    return redirect('/wall')

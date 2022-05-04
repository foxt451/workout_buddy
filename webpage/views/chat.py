from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.http import Http404

def room(request, user_id):
    if request.user.id == user_id:
        raise Http404()
    return render(request, 'webpage/chatroom.html', {
        'userFrom': {**model_to_dict(request.user, fields=['id', 'username']), 'userlink': request.user.get_absolute_url()},
        'userTo': {**model_to_dict((other := get_object_or_404(get_user_model(), id=user_id)), fields=['id', 'username']), 'userlink': other.get_absolute_url()}
    })
    
def chat_list(request):
    return render(request, 'webpage/chatrooms.html')
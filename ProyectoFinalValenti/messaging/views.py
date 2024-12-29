from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User

# VISTA PARA LA BANDEJA DE ENTRADA
@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messaging/inbox.html', {'messages': messages})

#VISTA PARA EL DETALLE DEL MENSAJE
@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id, receiver=request.user)
    message.is_read = True
    message.save()
    return render(request, 'messaging/message_detail.html', {'message': message})

#VISTA PARA ENVIAR MENSAJE
@login_required
def send_message(request):
    if request.method == 'POST':
        receiver_username = request.POST['receiver']
        subject = request.POST['subject']
        content = request.POST['content']

        receiver = User.objects.get(username=receiver_username)
        Message.objects.create(sender=request.user, receiver=receiver, subject=subject, content=content)

        return redirect('inbox')

    users = User.objects.exclude(username=request.user.username)
    return render(request, 'messaging/send_message.html', {'users': users})

def home(request):
    return render(request, 'messaging/home.html')
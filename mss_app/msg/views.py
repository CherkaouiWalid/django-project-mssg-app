from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Msg, MsgForm
from django.utils import timezone
from django.contrib.auth.models import User



def index(request):
    return  HttpResponse("Hello , world . you're at the messages index")

def msg(request):
    current_user=request.user
    if ( not request.user.is_authenticated):
        return HttpResponseRedirect('/accounts/login')
    else:
        messages= Msg.objects.filter(receiver=current_user)
        return render(request, "home.html", {'messages':messages})
def sentmsg(request):
    current_user=request.user
    if ( not request.user.is_authenticated):
        return HttpResponseRedirect('/accounts/login')
    else:
        messages=Msg.objects.filter(sender=current_user)
        return render(request, "sent_msgs.html", {'messages': messages})


def createMsg(request):
    current_user=request.user
    if ( not request.user.is_authenticated):
        return HttpResponseRedirect('/accounts/login')
    else:
        if request.method == 'POST':
            f = MsgForm(request.POST)
            if f.is_valid():
                instance=f.save(commit=False)
                instance.sender = current_user
                instance.datetime=timezone.now()
                instance.content=f.cleaned_data['content']
                instance.title=f.cleaned_data['title']
                instance.receiver=f.cleaned_data['receiver']
                instance.save()
                return HttpResponseRedirect('/msg/sent')
            else :
                return HttpResponse("form is not valid")
        else:
            f=MsgForm()
        return render(request, 'new_msg.html', {'form': f})








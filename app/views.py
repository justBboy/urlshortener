from django.shortcuts import render, redirect, reverse
from .models import Url
from .forms import UrlForm, SignUpForm
from .util import encodeId, decodeId
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    form = UrlForm(request.POST or None)
    shortenedId = ''
    sentUrl = ''
    host_name = request.get_host()
    shortenedUrl = ''


    if request.POST:
        if form.is_valid():
            url = request.POST.get('url')
            
            newUrl = Url(actualurl=url)
            newUrl.save()
            shortenedId = encodeId(newUrl.id)
            newUrl.shortenedid = shortenedId

            newUrl.save()
            
            if request.user.is_authenticated:
                request.user.url_set.create(actualurl=url, shortenedid=shortenedId)
            sentUrl = newUrl.actualurl
            shortenedUrl = '{}/{}'.format(host_name, shortenedId)

        
    context = {
        'form': form,
        'shortenedId': shortenedId,
        'sentUrl': sentUrl,
        'hostname': host_name,
        'shortenedUrl': shortenedUrl
    }
    return render(request, 'app/home.html', context=context)

def resolve_url(request, urlid):
    decodedId = decodeId(urlid)
    print(urlid)
    url = Url.objects.get(pk=decodedId)
    return redirect(url.actualurl)


def signUp(request):
    form = SignUpForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            newUser = User.objects.create(username=request.POST.get('username'), email=request.POST.get('email'))
            newUser.set_password(request.POST.get('password'))
            newUser.save()
            request.user = newUser
            return redirect('/')
    
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context=context)


from django.shortcuts import render, redirect
from .models import ModelData


def func(req):
    return render(req, 'home.html')


def ShortenUrl(req):
    if req.method == "POST":
        long_url = req.POST.get('long_url')
        obj = ModelData.shorten(long_url)
        return render(req, 'index.html', {
            'full_url': obj.long_url,
            'short_url': req.get_host() + '/' + obj.short_url,
            'a_url': 'https://' + obj.long_url,
        })
    return render(req, 'index.html')


def redirecttoURL(req, key):
    try:
        obj = ModelData.objects.get(short_url=key)
        url = 'https://' + obj.long_url
        return redirect(url)

    except:
        return redirect(ShortenUrl)


def URLROSTER(req):
    lst = ModelData.objects.all().values()
    urlList = {'urlList': lst}
    return render(req, 'urlRoster.html', urlList)

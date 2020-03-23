from django.shortcuts import render
from django.utils import timezone
from .models import Kakaomap
from django.shortcuts import render, get_object_or_404
from .forms import MapForm
from tkinter import messagebox



import logging as log

# Create your views here.

# mainpage라는 함수를 만든다.
# request요청을 받아 render메소드를 호출한다.


# 저장
def map_new(request):

    if request.method == "POST":
        # log.info("POST")
        form = MapForm(request.POST)
        if form.is_valid():
            # post = form(title=form.data['title'], text=form.data['text'], lat=form.data['lat'], long=form.data['long'] )
            post = form.save(commit=False)
            post.text = form.data['text']
            post.title = form.data['title']
            post.lat =  form.data['lat']
            post.long =  form.data['long']
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return render(request, 'second/map_new.html', {'form':form})
            # return redirect('map_new', pk=post.pk)

    else:
        form = MapForm()
    return render(request, 'second/map_new.html', {'form': form})


def mainpage(request):
    print('mainpage')
    form = MapForm()
    return render(request, 'second/mainpage.html', {'form': form})

def maplist(request):
    Kmap = Kakaomap.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'second/maplist.html', {'Kmap': Kmap})

def success(request):
    form = MapForm()
    return render(request, 'second/success.html', {'form': form})
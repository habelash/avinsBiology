from django.shortcuts import render
from django.http import Http404
from .models import LectureVideos
# Create your views here.


def index(request):
    context = {
        'videos': LectureVideos.objects.all()
    }
    return render(request, 'index.html', context)


def watch(request, play):
    try:
        display = LectureVideos.objects.get(id=play)
    except LectureVideos.DoesNotExist:
        raise Http404("Video Does Not Exist.")
    context = {
        'display': display,
        'videos': LectureVideos.objects.all()
    }
    return render(request, 'watch.html', context)


import pytube

from django.shortcuts import render
from django.http import FileResponse, HttpResponse


def index(request):
    return render(request, 'index.html')


def detail(request):
    video_url = request.POST['yt_video_url']
    global video
    video = pytube.YouTube(video_url)
    streams = video.streams.all()
    # for stream in streams:
    #     stream.
    return render(request, 'detail.html', {'video': video, 'streams': streams})


def yt_download(request):
    stream_itag = request.POST['stream_itag']
    stream = video.streams.get_by_itag(stream_itag)
    return FileResponse(open(stream.download(skip_existing=True), 'rb'), as_attachment=True)
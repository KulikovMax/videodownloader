from django.shortcuts import render, redirect
from django.http import FileResponse
import pytube


def index(request):
    return render(request, 'index.html')




def yt_download(request):
    try:
        video_url = request.POST['yt_video_url']
        yt = pytube.YouTube(video_url).streams.first()
        return FileResponse(open(yt.download(), 'rb'), as_attachment=True)
    except:
        return redirect(index)


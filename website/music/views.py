#from django.shortcuts import render

# Create your views here.
#def index(request):
   # return render(request, 'music/index.html')
#from django.http import HttpResponse
#from .models import Album

#def index(request):
    #all_albums = Album.objects.all()
    #html = ''
    #for album in all_albums:
        #url = '/music/' + str(album.id) + '/'       # not album_id, because it's object attribute "id" not album_id
        #html += '<a href="' + url + '">' + album.album_title + '</a><br>'

    #return HttpResponse(html)

#def detail(request, album_id): #def detail(request, album_id="1"):
    #return HttpResponse("<h2>Details for Album id:" + str(album_id) + "</h2>")

from django.http import HttpResponse
from django.template import loader
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
        }
    return HttpResponse(template.render(context, request))

def detail(request, album_id): #def detail(request, album_id="1"):
    return HttpResponse("<h2>Details for Album id:" + str(album_id) + "</h2>")
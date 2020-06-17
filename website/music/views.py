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



#from django.shortcuts import render, get_object_or_404
#from .models import Album


#def index(request):
   # all_albums = Album.objects.all()
   # return render(request, 'music/index.html', {'all_albums': all_albums})


#def detail(request, album_id): #def detail(request, album_id="1"):
   # album = get_object_or_404(Album, pk=album_id)
   # return render(request, 'music/detail.html', {'album': album})

#def favorite(request, album_id):
    #album = get_object_or_404(Album, pk=album_id)
    #try:
     #   selected_song = album.song_set.get(pk=request.POST['song'])
   # except (KeyError, Song.DoesNotExist):
    #    return render(request, 'music/detail.html', {
      #      'album': album,
      #      'error_message': "You did not select a valid song",
       #     })
   # else:
    #    selected_song.is_favorite = True
    #    selected_song.save()
     #   return render(request, 'music/detail.html', {'album': album})


from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
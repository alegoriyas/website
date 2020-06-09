"""
Definition of urls for website.
"""

from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic import RedirectView

#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    url(r'^music/', include('music.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/music/', permanent=True)),
    
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

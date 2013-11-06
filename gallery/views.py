from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from gallery.models import Gallery, Image

class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
   # context_object_name = 'latest_gallery_list'
    def get_queryset(self):
	    return Gallery.objects.filter(
	        pub_date__lte=timezone.now()
	    ).order_by('pub_date')[:5]

class GalleryView(generic.DetailView):
    model = Gallery
    template_name = 'gallery/gallery.html'
    def get_queryset(self):
        return Gallery.objects.filter(pub_date__lte=timezone.now())

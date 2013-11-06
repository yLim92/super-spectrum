from django.contrib import admin
from gallery.models import Gallery, Image

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

class GalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['category','desc']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ImageInline]
    list_display = ('title', 'pub_date', 'category','desc')
   # list_filter = ['pub_date']
    search_fields = ['category','title']
    date_hierarchy = 'pub_date'

admin.site.register(Gallery, GalleryAdmin)
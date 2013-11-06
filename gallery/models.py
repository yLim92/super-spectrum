from django.db import models
from django.core.files.storage import FileSystemStorage

class Gallery(models.Model):
	title = models.CharField(max_length=200)
	category = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	desc = models.TextField(max_length=None)
	def cover_photo(self):
		return self.image_set.all()[0]

fs = FileSystemStorage(location='gallery/static/gallery/media')

class Image(models.Model):
	gallery = models.ForeignKey(Gallery)
	title = models.CharField(max_length=200)
	desc = models.TextField(max_length=None)
	pub_date = models.DateTimeField('date published')
	photo = models.ImageField(storage=fs,upload_to='photos/%Y/%m/%d')
	#photo = models.ImageField(upload_to='photos/%Y/%m/%d')
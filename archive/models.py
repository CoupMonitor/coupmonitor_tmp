from django.db import models



# Create your models here.

class ImagePreview(models.Model):
        LargeImagePreviewLink = models.URLField() # Should be direct links to an image
        MediumImagePreviewLink = models.URLField()
        thumbnailImagePreviewLink = models.URLField()
        cachedImagePreview = models.ImageField()
        
class ResourceImage(models.Model):
        preview = models.ForeignKey('ImagePreview')
        
class ResourceVideo(models.Model):
        preview = models.ForeignKey('ImagePreview')
        VideoLink = models.URLField()   
        cachedVideo = models.FileField() # Any other video-specific way to support video uploads

class ResourceLiveStream(models.Model):
        preview = models.ForeignKey('ImagePreview')
        streamLink = models.URLField()
        cachedStream = models.FileField()       

class Resource(models.Model):
        resourceLink = models.URLField() # The main event link (fb,bambuser, youtube etc.)
        images = models.ForeignKey(ResourceImage)          
        videos = models.ForeignKey(ResourceVideo)
        streams = models.ForeignKey(ResourceLiveStream)
        source = models.TextField() # Rassd, MMN
        preview = models.ForeignKey(ImagePreview)



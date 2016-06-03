import os
import StringIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile

from PIL import Image

def get_image_path(instance, filename):
    return os.path.join('portraits', str(instance.student_id), filename)

def make_thumbnail(file):
    size = 256, 256
    img = Image.open(file)
    img.thumbnail((size), Image.ANTIALIAS)
    thumbnailString = StringIO.StringIO()
    img.save(thumbnailString, 'JPEG')
    newFile = InMemoryUploadedFile(thumbnailString, None, 'temp.jpg', 'image/jpeg', thumbnailString.len, None)

    return newFile

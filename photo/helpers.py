from os import listdir
from os.path import isfile, join

from photo.models import Photo
from photos.settings import MEDIA_ROOT


def include_all_files_from_media():
    onlyfiles = [f for f in listdir(MEDIA_ROOT) if isfile(join(MEDIA_ROOT, f))]
    Photo.objects.all().delete()
    for item in onlyfiles:
        if not Photo.objects.filter(image_url=item).exists():
            Photo.objects.create(image_url=item, name='Test')
    return onlyfiles

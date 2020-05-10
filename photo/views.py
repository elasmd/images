from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

# Create your views here.
from photo.helpers import include_all_files_from_media
from photo.models import Photo
from django.views.decorators.cache import cache_control


class ImageView(APIView):
    permission_classes = AllowAny,

    @cache_control(public=True, max_age="86400")
    def get(self, request):
        photo = Photo.objects.filter().order_by('last_accurance', 'id').first()
        photo.last_accurance = timezone.now()
        photo.save()
        return render(request, 'image.html', {'image': photo.image_url,
                                              'name': photo.name})


class ImageAddAll(APIView):
    def get(self, request):
        onlyfiles = include_all_files_from_media()
        return JsonResponse({"files": onlyfiles})

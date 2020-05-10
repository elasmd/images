from django.db import models


# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=256)
    image_url = models.CharField(max_length=256)
    last_accurance = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

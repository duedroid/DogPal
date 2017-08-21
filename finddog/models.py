from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='finddog_image/%Y/%m/')
    vector = models.TextField(blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name

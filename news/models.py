from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    url_to_image = models.CharField(max_length=100)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"

from django.db import models
from django.urls import reverse
# Create your models here.

class StandardPage(models.Model):
    """ Home model """

    heading = models.CharField(max_length=30, help_text="Page heading")

    ingress = models.CharField(max_length=100, help_text="ingress text")

    class Meta:
        ordering = ["-heading"]

    def get_absolute_url(self):
        "Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.heading

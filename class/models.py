from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Entry(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)

    # Providing various params to the model to take in
    #Images = models.ImageField(height_field=100, width_field=100)
    Company_name = models.CharField(max_length=500)
    discreption = models.TextField(blank=True, null=True)
    deatils = RichTextField(blank=True, null=True)
    last_date = models.DateTimeField(blank=True, null=True)
    application_url = models.URLField(max_length=1000, blank=True, null=True)
    #selected_students = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('class:Entry_detail', args=(str(self.id)))
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Company_name
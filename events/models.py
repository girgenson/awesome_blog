from django.db import models


class Event(models.Model):
    event_image = models.ImageField(upload_to='event_images/', name='image_of_event')
    event_text = models.CharField(max_length=300, name="text_of_event")

    def __str__(self):
        return self.text_of_event

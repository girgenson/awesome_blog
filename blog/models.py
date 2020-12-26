from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=50, name="title")
    date_of_post = models.DateTimeField(auto_now=True, name="date")
    text_post = models.TextField(name="entry")
    image_post = models.ImageField(upload_to='blog_images/', name='image')

    def get_summary(self):
        return self.entry[:70] + '...'

    def __str__(self):
        return self.title

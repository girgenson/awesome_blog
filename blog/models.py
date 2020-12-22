from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=50, name="Title")
    date_of_post = models.DateTimeField(auto_now=True)
    text_post = models.TextField(name="Entry")
    image_post = models.ImageField(upload_to='blog_images/', name='Image')

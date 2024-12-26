from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='post_images/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

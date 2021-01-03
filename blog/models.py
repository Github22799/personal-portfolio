from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog', blank=True)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

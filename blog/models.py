from django.db import models
import requests
from django.utils import timezone
from django_markdown.models import MarkdownField


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    id = models.CharField(max_length = 50, primary_key =True)

    text_html = models.TextField(blank=True)

    def convert_to_html(self):
        # lets Github know what type of data we are sending to them
        headers = {'Content-Type': 'text/plain'}
        data = self.text.encode('utf-8')
        # send a post request with the data
        r = requests.post('https://api.github.com/markdown/raw',headers=headers, data=data)
        return r.text.encode('utf-8')

    def save(self, *args, **kwargs):
        self.text_html = self.convert_to_html()
        super(Post, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
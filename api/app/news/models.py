from django.db import models


class News(models.Model):
    _id = models.CharField(max_length=300, primary_key=True)
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    published = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    language = models.CharField(max_length=300)

    class Meta:
        db_table = "rss_news"
        verbose_name_plural = "news"

    def __str__(self):
        return self.link

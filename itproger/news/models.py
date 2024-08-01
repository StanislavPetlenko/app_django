from django.db import models


class Article(models.Model):
    title = models.CharField('News name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    pub_date = models.DateTimeField('Publish date time')

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

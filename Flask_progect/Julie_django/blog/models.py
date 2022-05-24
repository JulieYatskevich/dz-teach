from cgitb import text
from django.db import models

class Post(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return f'Пост: {self.title}'

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'

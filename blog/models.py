from django.db import models
from datetime import datetime

from django.urls import reverse


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    body = models.TextField(verbose_name='Сам текст')
    photo = models.ImageField(verbose_name='Изображения блога', upload_to='images/', null=True, blank=True)
    photo1 = models.ImageField(verbose_name='Изображения блога', upload_to='images/', null=True, blank=True)
    photo2 = models.ImageField(verbose_name='Изображения блога', upload_to='images/', null=True, blank=True)
    photo3 = models.ImageField(verbose_name='Изображения блога', upload_to='images/', null=True, blank=True)
    photo4 = models.ImageField(verbose_name='Изображения блога', upload_to='images/', null=True, blank=True)
    photo5 = models.ImageField(verbose_name='Изображения блога', upload_to='images/', null=True, blank=True)
    photo6 = models.ImageField(verbose_name='Изображения блога', upload_to='images/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

#    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),

from django.db import models
from django.contrib.auth.models import User


class Animals(models.Model):
    title=models.CharField('Название', max_length=50)
    full_text=models.TextField("Описание")
    date=models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    obj = models.ForeignKey(Animals, verbose_name="Статья", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "bookmark"

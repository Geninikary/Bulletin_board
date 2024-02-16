from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse


class Author(models.Model):
    '''Авторы'''

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='author')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    '''Объявления'''

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    heading = models.CharField(max_length=300, verbose_name='Заголовок')
    text = RichTextField(max_length=2000, verbose_name='Статья')
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='PostCategory', verbose_name='Категория')

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse('post_one', args=[str(self.id)])


class Message(models.Model):
    '''Отклики'''

    on_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    msg_content = models.TextField(max_length=1000)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='отправитель', null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.msg_content


class Category(models.Model):
    '''Категории'''

    name_category = models.CharField(max_length=150)

    def __str__(self):
        return self.name_category


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

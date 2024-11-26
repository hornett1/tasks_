from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    STATUS_CHOICES = [
        ('not_started', 'Не начато'),
        ('in_progress', 'В процессе'),
        ('completed', 'Сделано')
    ]

    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий')
    ]

    name = models.CharField(max_length=50, verbose_name='Название', default="-")
    description = models.TextField(verbose_name="Описание", default="-")
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='not_started', verbose_name="Статус")
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=50, default='medium', verbose_name="Приоритет")
    start_date = models.DateTimeField(null=True, blank=True, verbose_name="Начало таска")
    end_date = models.DateTimeField(null=True, blank=True, verbose_name="Конец таска")
    task_author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="media", blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    
class Comment(models.Model):
    task = models.ForeignKey(Task, related_name="task", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
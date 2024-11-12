# Generated by Django 5.1.2 on 2024-11-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0002_alter_task_приоритет_alter_task_статус_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Конец таска',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Название',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Начало таска',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Описание',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Приоритет',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Статус',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='-', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Конец таска'),
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='-', max_length=50, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Низкий'), ('medium', 'Средний'), ('high', 'Высокий')], default='medium', max_length=50, verbose_name='Приоритет'),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Начало таска'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not_started', 'Не начато'), ('in_progress', 'В процессе'), ('completed', 'Сделано')], default='not_started', max_length=50, verbose_name='Статус'),
        ),
    ]

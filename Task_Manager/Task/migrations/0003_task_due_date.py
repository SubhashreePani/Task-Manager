# Generated by Django 4.2.2 on 2024-01-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.16 on 2024-11-15 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
    ]

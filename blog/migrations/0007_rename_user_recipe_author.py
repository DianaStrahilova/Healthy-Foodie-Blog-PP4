# Generated by Django 4.2.16 on 2024-10-29 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='user',
            new_name='author',
        ),
    ]
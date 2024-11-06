# Generated by Django 4.2.16 on 2024-11-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_post_comment_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default='recipe', max_length=200, unique=True),
        ),
    ]

# Generated by Django 4.2.16 on 2024-11-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
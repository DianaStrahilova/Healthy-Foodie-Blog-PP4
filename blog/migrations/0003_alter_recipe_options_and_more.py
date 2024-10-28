# Generated by Django 4.2.16 on 2024-10-28 21:52

from django.db import migrations
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_recipe_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-posted_date']},
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='created_on',
            new_name='posted_date',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='recipes/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=djrichtextfield.models.RichTextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=djrichtextfield.models.RichTextField(max_length=10000),
        ),
    ]

# Generated by Django 2.0.13 on 2019-07-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='280x150px', upload_to='blog/static/media/', verbose_name='Ссылка картинки'),
        ),
    ]

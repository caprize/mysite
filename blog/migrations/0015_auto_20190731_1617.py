# Generated by Django 2.0.13 on 2019-07-31 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_boturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='250x250px', upload_to='blog/static/media/', verbose_name='Ссылка картинки'),
        ),
    ]

# Generated by Django 3.2.22 on 2023-10-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse_planer', '0005_delete_userpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(default=1, upload_to='upload/', verbose_name='Blog Image'),
            preserve_default=False,
        ),
    ]
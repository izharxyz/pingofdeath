# Generated by Django 4.1.4 on 2022-12-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_id_blog_created_at_blog_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog_thumbnails'),
        ),
    ]
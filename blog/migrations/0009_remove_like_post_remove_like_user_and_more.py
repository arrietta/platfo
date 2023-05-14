# Generated by Django 4.2.1 on 2023-05-13 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_likes_post_likess_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='likess',
            new_name='likes',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]

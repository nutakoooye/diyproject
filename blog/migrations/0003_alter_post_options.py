# Generated by Django 3.2.8 on 2021-10-12 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211012_2241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_add'], 'permissions': (('can_create_new_post', 'Can create new post'),)},
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-17 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_usta_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usta',
            old_name='desc',
            new_name='aciklama',
        ),
        migrations.RenameField(
            model_name='usta',
            old_name='name',
            new_name='isim',
        ),
        migrations.RenameField(
            model_name='usta',
            old_name='category',
            new_name='kategori',
        ),
        migrations.RenameField(
            model_name='usta',
            old_name='image',
            new_name='resim',
        ),
    ]

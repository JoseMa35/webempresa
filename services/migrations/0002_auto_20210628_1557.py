# Generated by Django 3.2.3 on 2021-06-28 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Subtitulo'},
        ),
        migrations.RenameField(
            model_name='service',
            old_name='subtitile',
            new_name='subtitle',
        ),
    ]
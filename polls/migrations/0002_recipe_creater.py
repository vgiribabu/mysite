# Generated by Django 2.2.6 on 2019-11-06 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='creater',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]

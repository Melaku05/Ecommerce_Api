# Generated by Django 4.1.2 on 2022-10-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='image_url',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]

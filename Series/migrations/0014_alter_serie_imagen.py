# Generated by Django 5.1.4 on 2025-02-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Series', '0013_alter_serie_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='series_images/'),
        ),
    ]

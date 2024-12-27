# Generated by Django 5.1.3 on 2024-12-27 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_lanzamiento', models.DateField()),
                ('genero', models.CharField(max_length=100)),
                ('temporada', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='series_images/')),
            ],
        ),
    ]
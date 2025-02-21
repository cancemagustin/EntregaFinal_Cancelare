# Generated by Django 5.1.4 on 2025-02-21 12:52

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_lanzamiento', models.DateTimeField(auto_now_add=True)),
                ('reparto', models.CharField(default='Desconocido', max_length=255)),
                ('temporada', models.IntegerField()),
                ('plataformas', multiselectfield.db.fields.MultiSelectField(choices=[('flow', 'Flow'), ('disney_plus', 'Disney Plus'), ('max', 'Max'), ('amazon_prime', 'Amazon Prime'), ('paramount', 'Paramount'), ('apple_tv', 'Apple TV'), ('netflix', 'Netflix')], max_length=60)),
                ('imagen', models.ImageField(blank=True, upload_to='Series/')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion_serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.CharField(max_length=1000)),
                ('estrellas', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Series.serie')),
            ],
        ),
        migrations.CreateModel(
            name='SerieGenero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Series.generos')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Series.serie')),
            ],
            options={
                'unique_together': {('serie', 'genero')},
            },
        ),
        migrations.AddField(
            model_name='serie',
            name='generos',
            field=models.ManyToManyField(through='Series.SerieGenero', to='Series.generos'),
        ),
        migrations.CreateModel(
            name='SerieGuardada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Series.serie')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario', 'serie')},
            },
        ),
    ]

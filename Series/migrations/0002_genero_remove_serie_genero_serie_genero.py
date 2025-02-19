# Generated by Django 5.1.4 on 2025-01-03 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Series', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='serie',
            name='genero',
        ),
        migrations.AddField(
            model_name='serie',
            name='genero',
            field=models.ManyToManyField(related_name='series', to='Series.genero'),
        ),
    ]

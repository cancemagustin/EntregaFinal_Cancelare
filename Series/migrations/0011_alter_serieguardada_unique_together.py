# Generated by Django 5.1.4 on 2025-01-06 17:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Series', '0010_alter_serie_genero'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='serieguardada',
            unique_together={('usuario', 'serie')},
        ),
    ]
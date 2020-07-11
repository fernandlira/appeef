# Generated by Django 3.0.8 on 2020-07-11 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('disponibilidad', models.IntegerField(choices=[(0, 'Disponible'), (1, 'No disponible')], default=0)),
                ('puntuacion', models.FloatField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Conductor',
                'verbose_name_plural': 'Conductores',
            },
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('distrito', models.CharField(choices=[('LIMA_CERCADO', 'LIMA CERCADO'), ('ATE', 'ATE'), ('BARRANCO', 'BARRANCO'), ('LINCE', 'LINCE'), ('MIRAFLORES', 'MIRAFLORES')], max_length=60)),
                ('destino', models.CharField(max_length=255)),
                ('precio', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=0)),
                ('puntuacion', models.IntegerField(blank=True, choices=[(1, 'Malo'), (2, 'Regular'), (3, 'Neutro'), (4, 'Bueno'), (5, 'Excelente')], null=True)),
                ('conductor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appeff.Conductor')),
                ('viajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Viaje',
                'verbose_name_plural': 'Viajes',
            },
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('distrito', models.CharField(max_length=60)),
                ('destino', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Favorito',
                'verbose_name_plural': 'Favoritos',
            },
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=30)),
                ('placa', models.CharField(max_length=10)),
                ('anno', models.IntegerField(default=2000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Autos',
            },
        ),
    ]
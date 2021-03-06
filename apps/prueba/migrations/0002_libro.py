# Generated by Django 2.2.6 on 2019-11-02 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha Publicacion')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha Creacion')),
                ('autor_id', models.ManyToManyField(to='prueba.Autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-02 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor_id',
            field=models.ManyToManyField(null=True, to='prueba.Autor'),
        ),
    ]

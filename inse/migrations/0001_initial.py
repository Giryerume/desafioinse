# Generated by Django 5.0.1 on 2024-01-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sg_uf', models.CharField(max_length=2)),
                ('no_uf', models.CharField(max_length=100)),
                ('no_municipio', models.CharField(max_length=100)),
                ('no_escola', models.CharField(max_length=100)),
                ('inse_classificacao', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Haqqimizda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='Haqqimizda texti')),
                ('mission', models.TextField(verbose_name='Missiyamız və Vizyonumuz texti')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Basliq')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Adi ve siyadi')),
                ('position', models.CharField(max_length=100, verbose_name='Vezife')),
                ('detail', models.TextField(verbose_name='Haqqinizda')),
                ('email', models.CharField(max_length=100, verbose_name='mail address')),
            ],
        ),
    ]

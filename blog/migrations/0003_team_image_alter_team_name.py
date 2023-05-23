# Generated by Django 4.2.1 on 2023-05-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_haqqimizda_home_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.FileField(default=1, upload_to='', verbose_name='sekil'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Adi ve soyadi'),
        ),
    ]
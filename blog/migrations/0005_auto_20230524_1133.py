# Generated by Django 3.2.7 on 2023-05-24 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230523_0928'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='mehsullar',
            old_name='catagories',
            new_name='category',
        ),
    ]
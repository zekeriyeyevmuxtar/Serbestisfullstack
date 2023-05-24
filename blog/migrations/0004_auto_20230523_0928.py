# Generated by Django 3.2.7 on 2023-05-23 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_team_image_alter_team_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Mehsul kataqorisi')),
            ],
        ),
        migrations.AddField(
            model_name='mehsullar',
            name='catagories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.categories', verbose_name='Mehsul kateqoriyasi'),
        ),
    ]

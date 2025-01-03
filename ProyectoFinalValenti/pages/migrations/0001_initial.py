# Generated by Django 5.1.4 on 2024-12-29 22:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='pages/')),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

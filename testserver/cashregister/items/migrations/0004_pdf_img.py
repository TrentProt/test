# Generated by Django 4.2.7 on 2023-11-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
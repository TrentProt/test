# Generated by Django 4.2.7 on 2023-11-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_basket'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
            ],
        ),
    ]
# Generated by Django 3.2.5 on 2023-05-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextCorrection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_txt', models.TextField()),
                ('corrected_txt', models.TextField()),
            ],
        ),
    ]

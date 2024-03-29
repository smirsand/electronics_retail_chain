# Generated by Django 4.2.4 on 2024-01-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(choices=[('завод', 'завод'), ('ИП', 'ИП'), ('розничная сеть', 'розничная сеть')], max_length=50, verbose_name='звено сети')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('name', models.CharField(max_length=150, verbose_name='название организации')),
                ('country', models.CharField(max_length=150, verbose_name='страна')),
                ('city', models.CharField(max_length=150, verbose_name='город')),
                ('street', models.CharField(max_length=150, verbose_name='улица')),
                ('house_number', models.IntegerField(verbose_name='номер дома')),
            ],
            options={
                'verbose_name': 'звено',
                'verbose_name_plural': 'звено',
            },
        ),
    ]

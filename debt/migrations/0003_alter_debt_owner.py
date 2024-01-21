# Generated by Django 4.2.4 on 2024-01-20 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('debt', '0002_debt_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
            preserve_default=False,
        ),
    ]
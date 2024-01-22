# Generated by Django 4.2.4 on 2024-01-20 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='количество')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_as_buyer', to='links.link', verbose_name='покупатель')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_with_name', to='product.product', verbose_name='наименование товара')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_as_supplier', to='links.link', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'закупка',
                'verbose_name_plural': 'закупки',
            },
        ),
    ]

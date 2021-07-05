# Generated by Django 3.2.4 on 2021-07-02 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_cotizationfinancialintrument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='date',
            field=models.DateField(verbose_name='Purchase Date'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quantity',
            field=models.FloatField(verbose_name='Qnt'),
        ),
    ]
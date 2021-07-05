# Generated by Django 3.2.4 on 2021-07-01 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='brk_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='finance.broker'),
        ),
    ]

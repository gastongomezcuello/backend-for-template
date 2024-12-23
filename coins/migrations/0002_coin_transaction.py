# Generated by Django 5.1.3 on 2024-11-13 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='coins')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField()),
                ('transaction_type', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], max_length=4)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='coins.coin')),
            ],
        ),
    ]

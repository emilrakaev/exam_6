# Generated by Django 2.2 on 2020-08-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='status',
            field=models.TextField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=50, verbose_name='Статус'),
        ),
    ]
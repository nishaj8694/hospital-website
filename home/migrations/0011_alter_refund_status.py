# Generated by Django 4.2 on 2023-05-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refund',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'pending'), ('Process', 'Process'), ('cancel', 'cancel'), ('completed', 'completed')], default='pending', max_length=10, null=True),
        ),
    ]
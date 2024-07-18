# Generated by Django 4.2 on 2023-05-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_refund_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refund',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Process', 'Process'), ('cancel', 'cancel'), ('completed', 'completed')], default='pending', max_length=10, null=True),
        ),
    ]

# Generated by Django 4.2 on 2023-05-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_alter_wallet_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='contact_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

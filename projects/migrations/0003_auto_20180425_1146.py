# Generated by Django 2.0.4 on 2018-04-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180423_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_due',
            field=models.DateField(blank=True, null=True),
        ),
    ]
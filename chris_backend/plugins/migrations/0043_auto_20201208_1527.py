# Generated by Django 2.2.12 on 2020-12-08 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0042_auto_20201130_1317'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='plugin',
            unique_together={('meta', 'version'), ('meta', 'dock_image')},
        ),
    ]
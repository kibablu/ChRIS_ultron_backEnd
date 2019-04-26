# Generated by Django 2.1.4 on 2019-02-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipelines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultpipingboolparameter',
            name='value',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='defaultpipingfloatparameter',
            name='value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='defaultpipingintparameter',
            name='value',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='defaultpipingpathparameter',
            name='value',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='defaultpipingstrparameter',
            name='value',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
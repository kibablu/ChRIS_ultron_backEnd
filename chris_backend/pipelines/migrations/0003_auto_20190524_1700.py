# Generated by Django 2.1.4 on 2019-05-24 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0029_auto_20190423_1448'),
        ('pipelines', '0002_auto_20190221_2113'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='defaultpipingboolparameter',
            unique_together={('plugin_piping', 'plugin_param')},
        ),
        migrations.AlterUniqueTogether(
            name='defaultpipingfloatparameter',
            unique_together={('plugin_piping', 'plugin_param')},
        ),
        migrations.AlterUniqueTogether(
            name='defaultpipingintparameter',
            unique_together={('plugin_piping', 'plugin_param')},
        ),
        migrations.AlterUniqueTogether(
            name='defaultpipingpathparameter',
            unique_together={('plugin_piping', 'plugin_param')},
        ),
        migrations.AlterUniqueTogether(
            name='defaultpipingstrparameter',
            unique_together={('plugin_piping', 'plugin_param')},
        ),
    ]
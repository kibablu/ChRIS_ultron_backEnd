# Generated by Django 2.1.4 on 2019-02-01 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0026_auto_20190128_1615'),
        ('plugininstances', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PipelineInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=800)),
                ('pipeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='plugins.Pipeline')),
            ],
            options={
                'ordering': ('pipeline',),
            },
        ),
        migrations.AddField(
            model_name='plugininstance',
            name='pipeline_inst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plugin_instances', to='plugininstances.PipelineInstance'),
        ),
    ]
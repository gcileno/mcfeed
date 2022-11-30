# Generated by Django 4.1.3 on 2022-11-13 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_meta_vend_metas_vendedor_metas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendedor',
            name='metas',
        ),
        migrations.AddField(
            model_name='vendedor',
            name='metas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.metas'),
        ),
    ]

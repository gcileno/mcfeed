# Generated by Django 4.1.3 on 2022-12-01 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_filial_vendedor_filial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='filial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='filial', to='core.filial'),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='metas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meta', to='core.metas'),
        ),
    ]
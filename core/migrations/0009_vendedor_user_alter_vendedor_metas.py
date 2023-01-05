# Generated by Django 4.1.3 on 2022-12-11 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_alter_vendedor_filial_alter_vendedor_metas'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='metas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='metas', to='core.metas'),
        ),
    ]
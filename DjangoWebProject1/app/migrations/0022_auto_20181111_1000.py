# Generated by Django 2.1.2 on 2018-11-11 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20181110_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerta',
            name='tiempo',
        ),
        migrations.AddField(
            model_name='alerta',
            name='frecuencia',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alerta',
            name='periodicidad',
            field=models.CharField(choices=[('d', 'Dia'), ('h', 'Hora')], default='d', max_length=1),
        ),
        migrations.AlterField(
            model_name='nodo_no_led',
            name='lampara',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Lampara_No_LED'),
        ),
    ]

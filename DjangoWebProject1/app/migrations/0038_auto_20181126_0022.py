# Generated by Django 2.1.2 on 2018-11-26 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20181125_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marcador_luminaria_no_led',
            name='luminaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Lampara_No_LED'),
        ),
        migrations.AlterField(
            model_name='nodo_no_led',
            name='lampara',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Lampara_No_LED'),
        ),
        migrations.AlterField(
            model_name='notificacion_alerta',
            name='fecha_envio',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

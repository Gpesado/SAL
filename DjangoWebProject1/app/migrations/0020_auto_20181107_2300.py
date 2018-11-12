# Generated by Django 2.1.1 on 2018-11-08 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20181107_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marcador_grupo_luminaria',
            name='marcadoresLed',
        ),
        migrations.AddField(
            model_name='marcador_grupo_luminaria',
            name='marcadoresLed',
            field=models.ManyToManyField(blank=True, to='app.Marcador_Luminaria_Led'),
        ),
        migrations.RemoveField(
            model_name='marcador_grupo_luminaria',
            name='marcadoresNoLed',
        ),
        migrations.AddField(
            model_name='marcador_grupo_luminaria',
            name='marcadoresNoLed',
            field=models.ManyToManyField(blank=True, to='app.Marcador_Luminaria_No_Led'),
        ),
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
    ]

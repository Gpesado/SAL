# Generated by Django 2.1.2 on 2018-11-25 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20181125_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidente_reparador',
            name='materiales',
        ),
        migrations.AddField(
            model_name='incidente',
            name='materiales',
            field=models.ManyToManyField(to='app.Material'),
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

# Generated by Django 3.2 on 2023-08-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_piezasrepuesto_peso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piezasrepuesto',
            old_name='descripcion',
            new_name='observacion',
        ),
        migrations.AddField(
            model_name='piezasrepuesto',
            name='marca',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

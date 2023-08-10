# Generated by Django 3.2 on 2023-08-10 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bu', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atencion', models.CharField(max_length=50)),
                ('cliente', models.CharField(max_length=50)),
                ('ruc_dni', models.CharField(blank=True, max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=200)),
                ('obs', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Consultoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(blank=True, max_length=500)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='CotizacionConsultoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(blank=True, max_length=500)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='CotizacionManoDeObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(blank=True, max_length=500)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condicion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='ProformaManoDeObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('validez', models.CharField(max_length=20)),
                ('correo', models.CharField(blank=True, max_length=200)),
                ('celular', models.CharField(blank=True, max_length=9)),
                ('actividad', models.CharField(blank=True, max_length=500)),
                ('observacion', models.CharField(blank=True, max_length=500)),
                ('bu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.bu')),
                ('condicion_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.pago')),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.moneda')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='ProformaConsultoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('validez', models.CharField(max_length=20)),
                ('correo', models.CharField(blank=True, max_length=200)),
                ('celular', models.CharField(blank=True, max_length=9)),
                ('actividad', models.CharField(blank=True, max_length=500)),
                ('observacion', models.CharField(blank=True, max_length=500)),
                ('bu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.bu')),
                ('condicion_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.pago')),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.moneda')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Proforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('validez', models.CharField(max_length=20)),
                ('correo', models.CharField(blank=True, max_length=200)),
                ('celular', models.CharField(blank=True, max_length=9)),
                ('actividad', models.CharField(blank=True, max_length=500)),
                ('observacion', models.CharField(blank=True, max_length=500)),
                ('bu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.bu')),
                ('condicion_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.pago')),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.moneda')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='piezasRepuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=200)),
                ('marca', models.CharField(blank=True, max_length=100)),
                ('observacion', models.CharField(blank=True, max_length=200)),
                ('imagen_tienda', models.ImageField(blank=True, null=True, upload_to='imgPiezas')),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('peso', models.CharField(blank=True, max_length=50)),
                ('tipo_moneda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.moneda')),
            ],
        ),
        migrations.CreateModel(
            name='ManodeObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('tipo_moneda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.moneda')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='descripcionCotizacionManoDeObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=1000)),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('disponibilidad', models.CharField(max_length=20)),
                ('precio_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('descuento_tipo', models.CharField(choices=[('porcentaje', 'Porcentaje'), ('manual', 'Manual')], default='porcentaje', max_length=10)),
                ('descuento', models.IntegerField(choices=[(0, 'Sin descuento'), (5, '5%'), (10, '10%'), (15, '15%')], default=0)),
                ('descuento_manual', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('codigo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.manodeobra')),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cotizacionmanodeobra')),
            ],
        ),
        migrations.CreateModel(
            name='descripcionCotizacionConsultoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=1000)),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('disponibilidad', models.CharField(max_length=20)),
                ('precio_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('descuento_tipo', models.CharField(choices=[('porcentaje', 'Porcentaje'), ('manual', 'Manual')], default='porcentaje', max_length=10)),
                ('descuento', models.IntegerField(choices=[(0, 'Sin descuento'), (5, '5%'), (10, '10%'), (15, '15%')], default=0)),
                ('descuento_manual', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('codigo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.consultoria')),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cotizacionconsultoria')),
            ],
        ),
        migrations.CreateModel(
            name='descripcionCotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=1000)),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('disponibilidad', models.CharField(max_length=20)),
                ('precio_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('descuento_tipo', models.CharField(choices=[('porcentaje', 'Porcentaje'), ('manual', 'Manual')], default='porcentaje', max_length=10)),
                ('descuento', models.IntegerField(choices=[(0, 'Sin descuento'), (5, '5%'), (10, '10%'), (15, '15%')], default=0)),
                ('descuento_manual', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('codigo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.piezasrepuesto')),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cotizacion')),
            ],
        ),
        migrations.AddField(
            model_name='cotizacionmanodeobra',
            name='proforma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.proformamanodeobra'),
        ),
        migrations.AddField(
            model_name='cotizacionconsultoria',
            name='proforma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.proformaconsultoria'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='proforma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.proforma'),
        ),
    ]

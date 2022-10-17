# Generated by Django 3.2.13 on 2022-05-16 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0002_auto_20220516_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleado',
                'ordering': ['habilidad'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('trabajo', models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador'), ('2', 'Economista'), ('3', 'Otro')], max_length=1, verbose_name='Trabajo')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='empleado')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
                ('habilidades', models.ManyToManyField(to='persona.Habilidades')),
            ],
            options={
                'verbose_name': 'Registrar Empleado',
                'verbose_name_plural': 'Registrar Empleados',
                'ordering': ['nombre'],
                'unique_together': {('nombre', 'apellidos')},
            },
        ),
    ]
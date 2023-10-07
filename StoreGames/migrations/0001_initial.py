from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),  # Cambiado de 'apellidos' a 'apellido'
                ('correo', models.EmailField(max_length=254)),
                ('usuario', models.CharField(max_length=16)),
                ('contrasena', models.CharField(max_length=12)),  # Cambiado de 'contrasena' a 'pass'
                ('fechanacimiento', models.DateField()),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

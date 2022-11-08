from django.db import migrations
import datetime




def creardata(apps, schema_editor):
    Fam = apps.get_model('appFamilia', 'Familiar')
    Fam.objects.create(id=1, nombre='Sandra', edad=60, relacion="Madre", ocupacion='Administracion', fechanac=datetime.datetime(1962,1,5))
    Fam.objects.create(id=2, nombre='Alfonso', edad=62, relacion="Padre", ocupacion='Comerciante', fechanac=datetime.datetime(1960,8,2))
    Fam.objects.create(id=3, nombre='Diego', edad=34, relacion="Hermano", ocupacion='Educacion', fechanac=datetime.datetime(1987,11,9))
    Fam.objects.create(id=4, nombre='Rufina', edad=87, relacion="Abuela", ocupacion='Jubilada', fechanac=datetime.datetime(1935,8,24))


class Migration(migrations.Migration):

    dependencies = [
         ('appFamilia', '0002_familiar_fechanac'),
    ]

    operations = [
      migrations.RunPython(creardata),
    ]
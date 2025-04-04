# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Entradas(models.Model):
    codentrada = models.IntegerField(primary_key=True)
    numfila = models.IntegerField(blank=True, null=True)
    numenfila = models.IntegerField(blank=True, null=True)
    codpase = models.ForeignKey('Pases', models.DO_NOTHING, db_column='codpase', blank=True, null=True)
    vendido = models.CharField(max_length=1, blank=True, null=True)
    comprador = models.CharField(max_length=60, blank=True, null=True)
    pvp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ENTRADAS'


class Pases(models.Model):
    codpase = models.IntegerField(primary_key=True)
    codsala = models.ForeignKey('Salas', models.DO_NOTHING, db_column='codsala')
    codpelicula = models.ForeignKey('Peliculas', models.DO_NOTHING, db_column='codpelicula')
    fecha_pase = models.DateField()
    tipo_pase = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PASES'


class Peliculas(models.Model):
    codpelicula = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=60)
    fecha_prod = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PELICULAS'


class Salas(models.Model):
    codsala = models.IntegerField(primary_key=True)
    tipo_sonido = models.CharField(max_length=10, blank=True, null=True)
    numfilas = models.IntegerField(blank=True, null=True)
    numasiporfilas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SALAS'

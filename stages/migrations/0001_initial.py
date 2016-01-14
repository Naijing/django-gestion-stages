# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('libelle', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, blank=True, null=True)),
                ('telephone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=250)),
                ('codePostal', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=50)),
                ('pays', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=20)),
                ('latitude', models.DecimalField(max_digits=13, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=13, decimal_places=10)),
            ],
        ),
        migrations.CreateModel(
            name='GestionDeTaxe',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('taxePaye', models.CharField(max_length=3, choices=[('OUI', 'OUI'), ('NON', 'NON')])),
                ('dateTaxe', models.DateTimeField()),
                ('dateContact', models.DateTimeField()),
                ('modalite', models.CharField(max_length=10, choices=[('email', 'Email'), ('tel', 'Tel'), ('courrier', 'Courrier')])),
                ('contact', models.ForeignKey(related_name='contact', to='stages.Contact')),
                ('entreprise', models.ForeignKey(related_name='gestiondetaxe', to='stages.Entreprise')),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('code', models.PositiveSmallIntegerField(unique=True)),
                ('alpha2', models.CharField(unique=True, max_length=2)),
                ('alpha3', models.CharField(unique=True, max_length=3)),
                ('nom_en_gb', models.CharField(max_length=45)),
                ('nom_fr_fr', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='VillesDeFrance',
            fields=[
                ('id', models.AutoField(primary_key=True, db_column='ville_id', serialize=False)),
                ('departement', models.CharField(max_length=3, db_column='ville_departement')),
                ('slug', models.CharField(max_length=255, db_column='ville_slug')),
                ('nom', models.CharField(max_length=45, db_column='ville_nom')),
                ('nom_reel', models.CharField(max_length=45, db_column='ville_nom_reel')),
                ('nom_soundex', models.CharField(max_length=45, db_column='ville_nom_soundex')),
                ('nom_metaphone', models.CharField(max_length=45, db_column='ville_nom_metaphone')),
                ('code_postal', models.CharField(max_length=255, db_column='ville_code_postal')),
                ('commune', models.CharField(max_length=3, db_column='ville_commune')),
                ('code_commune', models.CharField(max_length=5, db_column='ville_code_commune')),
                ('arrondissement', models.PositiveSmallIntegerField(db_column='ville_arrondissement')),
                ('canton', models.CharField(max_length=4, db_column='ville_canton')),
                ('amdi', models.PositiveSmallIntegerField(db_column='ville_amdi')),
                ('population_2010', models.PositiveIntegerField(db_column='ville_population_2010')),
                ('population_1999', models.PositiveIntegerField(db_column='ville_population_1999')),
                ('population_2012', models.PositiveIntegerField(db_column='ville_population_2012')),
                ('densite_2010', models.IntegerField(db_column='ville_densite_2010')),
                ('surface', models.PositiveIntegerField(db_column='ville_surface')),
                ('longitude_deg', models.FloatField(db_column='ville_longitude_deg')),
                ('latitude_deg', models.FloatField(db_column='ville_latitude_deg')),
                ('longitude_grd', models.CharField(max_length=9, db_column='ville_longitude_grd')),
                ('latitude_grd', models.CharField(max_length=8, db_column='ville_latitude_grd')),
                ('longitude_dms', models.CharField(max_length=9, db_column='ville_longitude_dms')),
                ('latitude_dms', models.CharField(max_length=8, db_column='ville_latitude_dms')),
                ('zmin', models.IntegerField(db_column='ville_zmin')),
                ('zmax', models.IntegerField(db_column='ville_zmax')),
                ('population_2010_order_france', models.IntegerField(db_column='ville_population_2010_order_france')),
                ('densite_2010_order_france', models.IntegerField(db_column='ville_densite_2010_order_france')),
                ('surface_order_france', models.IntegerField(db_column='ville_surface_order_france')),
            ],
            options={
                'db_table': 'villes_france',
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='entreprise',
            field=models.ForeignKey(related_name='contacts', to='stages.Entreprise'),
        ),
    ]

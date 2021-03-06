# Generated by Django 3.0.6 on 2020-05-28 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compagnie', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('civilite', models.CharField(choices=[('monsieur', 'Monsieur'), ('madame', 'Madame')], max_length=20)),
                ('date_de_naissance', models.DateField()),
                ('lieu_de_naissance', models.CharField(max_length=250)),
                ('grade', models.CharField(max_length=20)),
                ('compagnies', models.ForeignKey(default='MNS', on_delete=django.db.models.deletion.DO_NOTHING, to='Diplome.Compagnie')),
            ],
        ),
        migrations.CreateModel(
            name='TypeSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_session', models.CharField(max_length=255)),
                ('nom_complet', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feuille_de_renseignement', models.CharField(choices=[('pas fait', 'Pas fait'), ('transmit', 'Transmit'), ('retour', 'Retour')], default='pas fait', max_length=20)),
                ('proces_verbal', models.CharField(choices=[('pas fait', 'Pas fait'), ('transmit', 'Transmit'), ('retour', 'Retour')], default='pas fait', max_length=20)),
                ('diplome', models.CharField(choices=[('pas fait', 'Pas fait'), ('signature seccc', 'Signature SecCC'), ('ventile', 'Ventilés')], default='pas fait', max_length=20)),
                ('numero_de_session', models.IntegerField()),
                ('date_de_debut', models.DateField()),
                ('date_de_fin', models.DateField()),
                ('formateur', models.CharField(max_length=50, null=True)),
                ('archive', models.BooleanField(default=False)),
                ('compagnies', models.ForeignKey(default='MNS', on_delete=django.db.models.deletion.DO_NOTHING, to='Diplome.Compagnie')),
                ('personnes', models.ManyToManyField(blank=True, to='Diplome.Personne')),
                ('type_sessions', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='type_sessions', to='Diplome.TypeSession')),
            ],
        ),
        migrations.CreateModel(
            name='Diplomes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aptitude', models.CharField(choices=[('apte', 'Apte'), ('inapte', 'Inapte')], max_length=20)),
                ('numero_diplome', models.IntegerField()),
                ('personne_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Diplome.Personne')),
                ('session_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Diplome.TypeSession')),
            ],
        ),
    ]

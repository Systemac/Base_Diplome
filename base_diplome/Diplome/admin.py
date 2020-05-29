from django.contrib import admin
from .models import Session, Diplomes, Personne, TypeSession, Compagnie


# Register your models here.

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = [
        'type_sessions',
        'feuille_de_renseignement',
        'proces_verbal',
        'diplome',
        'numero_de_session',
        'date_de_debut',
        'date_de_fin',
        'compagnies',
        'formateur',
    ]


@admin.register(Compagnie)
class CompagnieAdmin(admin.ModelAdmin):
    list_display = [
        'compagnie',
    ]


@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    list_display = [
        'nom',
        'prenom',
        'civilite',
        'date_de_naissance',
        'lieu_de_naissance',
        'grade',
        'compagnies',
    ]


@admin.register(TypeSession)
class TypeSesionAdmin(admin.ModelAdmin):
    list_display = [
        'type_session',
        'nom_complet'
    ]

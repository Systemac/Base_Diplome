from django.db import models


# Create your models here.
class Session(models.Model):
    STATUS_FR_PF = 'pas fait'
    STATUS_FR_TR = 'transmit'
    STATUS_FR_R = 'retour'

    STATUS_DP_PF = 'pas fait'
    STATUS_DP_SCC = 'signature seccc'
    STATUS_DP_V = 'ventile'

    STATUS_FR_CHOICES = (
        (STATUS_FR_PF, 'Pas fait'),
        (STATUS_FR_TR, 'Transmit'),
        (STATUS_FR_R, 'Retour'),)

    STATUS_DP_CHOICES = (
        (STATUS_DP_PF, 'Pas fait'),
        (STATUS_DP_SCC, 'Signature SecCC'),
        (STATUS_DP_V, 'Ventilés'),)

    feuille_de_renseignement = models.CharField(max_length=20,
                                                default=STATUS_FR_PF,
                                                choices=STATUS_FR_CHOICES)
    proces_verbal = models.CharField(max_length=20,
                                     default=STATUS_FR_PF,
                                     choices=STATUS_FR_CHOICES)
    diplome = models.CharField(max_length=20,
                               default=STATUS_DP_PF,
                               choices=STATUS_DP_CHOICES)
    type_sessions = models.ForeignKey('typesession',
                                      on_delete=models.DO_NOTHING,
                                      blank=False,
                                      null=False,
                                      related_name='type_sessions')
    numero_de_session = models.IntegerField(null=False,
                                            blank=False)
    date_de_debut = models.DateField()
    date_de_fin = models.DateField()
    compagnies = models.ForeignKey('compagnie',
                                   on_delete=models.DO_NOTHING,
                                   default='MNS')
    formateur = models.CharField(max_length=50,
                                 null=True)
    archive = models.BooleanField(default=False)
    personnes = models.ManyToManyField('personne',
                                       blank=True, )

    def __str__(self):
        return self.type_sessions.type_session

    def get_pacs(self):
        return [p for p in self.personnes.all()]


class Personne(models.Model):
    STATUS_MON = 'monsieur'
    STATUS_MME = 'madame'
    STATUS_CHOICES = (
        (STATUS_MON, 'Monsieur'),
        (STATUS_MME, 'Madame'),
    )
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    civilite = models.CharField(max_length=20,
                                choices=STATUS_CHOICES)
    date_de_naissance = models.DateField()
    lieu_de_naissance = models.CharField(max_length=250)
    grade = models.CharField(max_length=20)
    compagnies = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Diplomes(models.Model):
    STATUS_APT_OK = 'apte'
    STATUS_APT_NOK = 'inapte'

    STATUS_CHOICES = (
        (STATUS_APT_OK, 'Apte'),
        (STATUS_APT_NOK, 'Inapte'),)
    session_id = models.OneToOneField('typesession',
                                      on_delete=models.CASCADE,
                                      null=True)
    personne_id = models.OneToOneField('personne',
                                       on_delete=models.CASCADE,
                                       null=True)
    aptitude = models.CharField(max_length=20,
                                choices=STATUS_CHOICES)
    numero_diplome = models.IntegerField()


class TypeSession(models.Model):
    type_session = models.CharField(max_length=255)
    nom_complet = models.CharField(max_length=255)

    def __str__(self):
        return self.type_session


class Compagnie(models.Model):
    compagnie = models.CharField(max_length=30)

    def __str__(self):
        return self.compagnie

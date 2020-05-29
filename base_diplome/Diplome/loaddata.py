# Full path and name to your csv file
csv_session = "F:\\Dev\\Base_Diplome\\base_diplome\\Diplome\\Tsession.csv"
csv_compagnie = "F:\\Dev\\Base_Diplome\\base_diplome\\Diplome\\Compagnie.csv"
csv_personne = "F:\\Dev\\Base_Diplome\\base_diplome\\Diplome\\Personne.csv"
import datetime
import csv

from Diplome.models import Compagnie, TypeSession, Personne

df_session = csv.reader(open(csv_session), delimiter=',', quotechar='"')
df_compagnie = csv.reader(open(csv_compagnie), delimiter=',', quotechar='"')
df_personne = csv.reader(open(csv_personne), delimiter=',', quotechar='"')

for row in df_session:
    if row[0] != 'type_sessions':
        if len(TypeSession.objects.filter(type_session__icontains=row[0])) == 0:
            tsession = TypeSession()
            tsession.type_session = row[0]
            tsession.nom_complet = row[1]
            tsession.save()

for row in df_personne:
    if row[0] != 'NOM':
        if row[0] != '':
            nom = row[0].upper()
            prenom = row[1].capitalize()
            civilite = row[2].lower()
            ddn = datetime.datetime.strptime(row[3], '%d/%m/%Y')
            ldn = row[4]
            grade = row[9]
            compagnie = row[10]
            if len(Personne.objects.filter(nom__icontains=nom)) == 0:
                if len(Personne.objects.filter(date_de_naissance__icontains=ddn)) == 0:
                    personne = Personne()
                    compagnies = Compagnie()
                    personne.nom = nom.upper()
                    personne.prenom = prenom
                    personne.civilite = civilite
                    personne.date_de_naissance = ddn
                    personne.lieu_de_naissance = ldn
                    personne.grade = grade
                    personne.compagnies = compagnie
                    print(personne)
                    personne.save()

for row in df_compagnie:
    if row[0] != 'COMPAGNIE':  # Ignore the header row, import everything else
        if len(Compagnie.objects.filter(compagnie__icontains=row[0])) == 0:
            Type_session = Compagnie()
            Type_session.compagnie = row[0]
            Type_session.save()

quit()

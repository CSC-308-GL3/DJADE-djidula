class Grade:
    def __init__(self, code, libelle, taux):
        self.code = code
        self.libelle = libelle
        self.taux = taux

    def getCode(self):
        return self.code

    def getLibelle(self):
        return self.libelle

    def tauxHoraire(self):
        return self.taux


class Employe:
    def __init__(self, numero, nom, qualification, dateEmbauche):
        self.numero = numero
        self.nom = nom
        self.qualification = qualification
        self.dateEmbauche = dateEmbauche

    def coutHoraire(self):
        anciennete = self.getAnciennete(self.dateEmbauche)
        coeff = 1.0
        if anciennete >= 5 and anciennete <= 10:
            coeff = 1.05
        elif anciennete >= 11 and anciennete <= 15:
            coeff = 1.08
        elif anciennete > 15:
            coeff = 1.12
        return self.qualification.tauxHoraire() * coeff

    def getNumero(self):
        return self.numero

    def getNom(self):
        return self.nom

    def getQualification(self):
        return self.qualification

    def getDateEmbauche(self):
        return self.dateEmbauche

    def getAnciennete(self, date):
    	annee_embauche = int(self.dateEmbauche[:4])
     	annee_courante = datetime.now().year
     	return annee_courante - annee_embauche


class Client:
    def __init__(self, numero, nom, adresse, codePostale, ville, nbKm):
        self.numero = numero
        self.nom = nom
        self.adresse = adresse
        self.codePostale = codePostale
        self.ville = ville
        self.nbKm = nbKm

    def distance(self):
         return self.nbKm


class Intervention:
    def __init__(self, numero, date, duree, tarifKm, technicien):
        self.numero = numero
        self.date = date
        self.duree = duree
        self.tarifKm = tarifKm
        self.technicien = technicien

    def affiche(self):
        print(f"Intervention #{self.numero}")
        print(f"Date: {self.date}")
        print(f"Duree: {self.duree}")
        print(f"Tarif Kilometrique: {self.tarifKm}")
        print("Technicien:")
        self.technicien.affiche()

    def fraisKm(self, dist):
        return self.tarifKm * dist

    def fraisMo(self):
        return self.duree * self.technicien.coutHoraire()


class Contrat:
    def __init__(self, numero, date, client, montantContrat, interventions):
        self.numero = numero
        self.date = date
        self.client = client
        self.montantContrat = montantContrat
        self.interventions = interventions
        self.nbIntervention = len(interventions)

    def montant(self):
        return self.montantContrat

    def ecart(self):
        totalInterventionCost = sum(
            intervention.fraisKm(self.client.distance()) + intervention.fraisMo() for intervention in self.interventions
        )
        return self.montantContrat - totalInterventionCost

    def affiche(self):
        print(f"Contrat #{self.numero}")
        print(f"Date: {self.date}")
        print(f"Client: {self.client.nom}")
        print(f"Montant: {self.montantContrat}")
        print(f"Nombre d'interventions: {self.nbIntervention}")
        print("Interventions:")
        for intervention in self.interventions:
            intervention.affiche()

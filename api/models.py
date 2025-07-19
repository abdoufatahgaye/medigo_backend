from django.db import models

class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    mot_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.nom

class Traitement(models.Model):
    nom_medicament = models.CharField(max_length=100)
    frequence = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom_medicament} - {self.utilisateur}"

class Consultation(models.Model):
    date = models.DateTimeField()
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    lieu = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.utilisateur} - {self.medecin} - {self.date}"

class Message(models.Model):
    emetteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_envoyes')
    recepteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_recus')
    contenu = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.emetteur} à {self.recepteur}"

class Etablissement(models.Model):
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    telephone = models.CharField(max_length=20)
    horaires_ouverture = models.TimeField()
    horaires_fermeture = models.TimeField()

    def __str__(self):
        return self.nom

class StockPharmacie(models.Model):
    pharmacie = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    medicament = models.CharField(max_length=100)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.medicament} - {self.pharmacie}"

class EvaluationMedecin(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    note = models.IntegerField()

    class Meta:
        unique_together = ['utilisateur', 'medecin']

    def __str__(self):
        return f"{self.utilisateur} - {self.medecin} - {self.note}"

class Campagne(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    ordonnance_scan = models.ImageField(upload_to='ordonnances/')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Campagne de {self.utilisateur}"

class Donation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    campagne = models.ForeignKey(Campagne, on_delete=models.CASCADE)
    operateur = models.CharField(max_length=50)
    numero_telephone = models.CharField(max_length=20)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.utilisateur} - {self.montant}"


class Ordonnance(models.Model):
    image = models.ImageField(upload_to='ordonnances/')
    medicaments_extraits = models.TextField(blank=True, null=True)
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ordonnance #{self.id}"

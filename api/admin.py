from django.contrib import admin
from .models import User, Medecin, Traitement, Consultation, Message, Etablissement, StockPharmacie, EvaluationMedecin, Campagne, Donation

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'telephone')
    search_fields = ('nom', 'prenom', 'telephone')

@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'specialite', 'telephone', 'rating')
    search_fields = ('nom', 'specialite')

@admin.register(Traitement)
class TraitementAdmin(admin.ModelAdmin):
    list_display = ('nom_medicament', 'utilisateur', 'date_debut', 'date_fin')
    list_filter = ('date_debut', 'date_fin')

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'medecin', 'date', 'lieu')
    list_filter = ('date', 'medecin')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('emetteur', 'recepteur', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'telephone')
    search_fields = ('nom', 'type')

@admin.register(StockPharmacie)
class StockPharmacieAdmin(admin.ModelAdmin):
    list_display = ('pharmacie', 'medicament', 'quantite')
    list_filter = ('pharmacie',)

@admin.register(EvaluationMedecin)
class EvaluationMedecinAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'medecin', 'note')
    list_filter = ('medecin', 'note')

@admin.register(Campagne)
class CampagneAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'date_creation')
    list_filter = ('date_creation',)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'campagne', 'montant', 'operateur')
    list_filter = ('operateur', 'campagne')

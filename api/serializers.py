from rest_framework import serializers
from .models import User, Medecin, Traitement, Consultation, Message, Etablissement, StockPharmacie, EvaluationMedecin, Campagne, Donation, Ordonnance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nom', 'prenom', 'telephone', 'mot_de_passe']

class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = ['id', 'nom', 'specialite', 'telephone', 'rating']

class TraitementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traitement
        fields = ['id', 'nom_medicament', 'frequence', 'date_debut', 'date_fin', 'utilisateur']

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'date', 'medecin', 'utilisateur', 'lieu']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'emetteur', 'recepteur', 'contenu', 'timestamp']

class EtablissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etablissement
        fields = ['id', 'nom', 'type', 'latitude', 'longitude', 'telephone', 'horaires_ouverture', 'horaires_fermeture']

class StockPharmacieSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPharmacie
        fields = ['id', 'pharmacie', 'medicament', 'quantite']

class EvaluationMedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationMedecin
        fields = ['id', 'utilisateur', 'medecin', 'note']

class CampagneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campagne
        fields = ['id', 'utilisateur', 'description', 'ordonnance_scan', 'date_creation']

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'utilisateur', 'campagne', 'operateur', 'numero_telephone', 'montant']

from .models import Ordonnance

class OrdonnanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordonnance
        fields = ['id', 'image', 'medicaments_extraits', 'date_upload']
        read_only_fields = ['medicaments_extraits', 'date_upload'] 
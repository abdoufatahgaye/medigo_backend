from rest_framework import viewsets
from .models import User, Medecin, Traitement, Consultation, Message, Etablissement, StockPharmacie, EvaluationMedecin, Campagne, Donation
from .serializers import UserSerializer, MedecinSerializer, TraitementSerializer, ConsultationSerializer, MessageSerializer, EtablissementSerializer, StockPharmacieSerializer, EvaluationMedecinSerializer, CampagneSerializer, DonationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

class TraitementViewSet(viewsets.ModelViewSet):
    queryset = Traitement.objects.all()
    serializer_class = TraitementSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class EtablissementViewSet(viewsets.ModelViewSet):
    queryset = Etablissement.objects.all()
    serializer_class = EtablissementSerializer

class StockPharmacieViewSet(viewsets.ModelViewSet):
    queryset = StockPharmacie.objects.all()
    serializer_class = StockPharmacieSerializer

class EvaluationMedecinViewSet(viewsets.ModelViewSet):
    queryset = EvaluationMedecin.objects.all()
    serializer_class = EvaluationMedecinSerializer

class CampagneViewSet(viewsets.ModelViewSet):
    queryset = Campagne.objects.all()
    serializer_class = CampagneSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

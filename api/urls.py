from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MedecinViewSet, TraitementViewSet, ConsultationViewSet, MessageViewSet, EtablissementViewSet, StockPharmacieViewSet, EvaluationMedecinViewSet, CampagneViewSet, DonationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'medecins', MedecinViewSet)
router.register(r'traitements', TraitementViewSet)
router.register(r'consultations', ConsultationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'etablissements', EtablissementViewSet)
router.register(r'stocks', StockPharmacieViewSet)
router.register(r'evaluations', EvaluationMedecinViewSet)
router.register(r'campagnes', CampagneViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
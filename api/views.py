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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import OrdonnanceSerializer
from .models import Ordonnance
import google.generativeai as genai
from PIL import Image
import io

class OrdonnanceUploadAPIView(APIView):
    """
    API endpoint pour télécharger une ordonnance et extraire les médicaments.
    """
    def post(self, request, *args, **kwargs):
        serializer = OrdonnanceSerializer(data=request.data)
        if serializer.is_valid():
                
            print("Le serializer est valide !")
            # Sauvegardez l'image d'abord, mais ne committez pas encore le modèle pour pouvoir le modifier
            ordonnance = serializer.save()

            # Vérifiez si une image a été uploadée
            if not ordonnance.image:
                return Response(
                    {"error": "Aucune image n'a été fournie."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Configurez l'API Gemini
            genai.configure(api_key=settings.GEMINI_API_KEY)

            try:
                # Lisez l'image du fichier temporaire et transformez-la en objet PIL Image
                # L'image est un InMemoryUploadedFile, vous pouvez y accéder directement
                img_data = ordonnance.image.read()
                img = Image.open(io.BytesIO(img_data))

                # Initialiser le modèle Gemini Vision
                model = genai.GenerativeModel('gemini-1.5-flash')

                # Prompt pour extraire les médicaments
                prompt = (
                    "Extrait uniquement la liste des médicaments présents sur cette ordonnance médicale. Donnes juste le nom des médicaments."
                    "Réponds avec une liste numérotée, chaque élément étant le nom du médicament. "
                    "Pour les réponses met juste le nom des médicaments sans texte supplémentaire ex: 'parecetamol, amoxiciline' "
                    "Si tu n'es pas certain, indique 'Inconnu'. Si ce n'est pas un médicament mets juste inconnu. "
                    "Voici l'image de l'ordonnance :"
                )

                # Envoyer l'image et le prompt au modèle Gemini
                response = model.generate_content([prompt, img])
                medicaments_extraits = response.text

            except Exception as e:
                # Gérer les erreurs de l'API Gemini ou de traitement d'image
                return Response(
                    {"error": f"Erreur lors de l'extraction des médicaments : {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            ordonnance.medicaments_extraits = medicaments_extraits
            ordonnance.save() # Sauvegardez le modèle après avoir ajouté les médicaments

            # Renvoyez la représentation sérialisée de l'ordonnance sauvegardée
            return Response(OrdonnanceSerializer(ordonnance).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdonnanceDetailAPIView(APIView):
    """
    API endpoint pour récupérer les détails d'une ordonnance spécifique.
    """
    def get(self, request, pk, *args, **kwargs):
        try:
            ordonnance = Ordonnance.objects.get(pk=pk)
            serializer = OrdonnanceSerializer(ordonnance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Ordonnance.DoesNotExist:
            return Response(
                {"error": "Ordonnance non trouvée."},
                status=status.HTTP_404_NOT_FOUND
            )
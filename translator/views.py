from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer
import google.generativeai as genai
from drf_yasg.utils import swagger_auto_schema
import os

# Create your views here.
os.environ["GOOGLE_API_KEY"] = ""
api_key = os.environ["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
    
class AllTranslation(APIView):
    
    @swagger_auto_schema(responses={200: TranslationSerializer(many=True)})
    def get(self, request):

        result = Translation.objects.all()
        serializer_data = TranslationSerializer(result, many=True)

        return Response(data=serializer_data.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(responses={201: TranslationSerializer})
    def post(self, request):

        source_language = "FR"
        source_text = "Salut, je m'appelle Paul !"
        target_language = "ES"

        if not source_language or not target_language or not source_text:
            return Response({"detail": "Il manque des champs nécessaires!"}, status=status.HTTP_400_BAD_REQUEST)

        if Translation.objects.filter(source_language=source_language, source_text=source_text, target_language=target_language).exists():
            return Response({"detail": "La traduction existe déjà"}, status=status.HTTP_400_BAD_REQUEST)

        prompt = f'Traduis "{source_text}" de {source_language} en {target_language}. La réponse ne doit contenir que la traduction.'
        response = model.generate_content(prompt)

        if not response or not response.text:
            return Response({"detail": "Erreur de l'API Gemini"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        target_text = response.text.strip()

        translation = Translation.objects.create(
            source_language=source_language,
            source_text=source_text,
            target_language=target_language,
            target_text=target_text
        )
        serializer_data = TranslationSerializer(translation)

        return Response(data=serializer_data.data, status=status.HTTP_201_CREATED)

def index(request):
    return render(request, 'index.html', context={})
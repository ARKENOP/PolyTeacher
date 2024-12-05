from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer
import google.generativeai as genai

# Create your views here.

class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):

        data = Translation.objects.filter(source_language__in=['FR', 'ES'], target_language__in=['FR', 'ES'])  
        serialized_data = TranslationSerializer(data, many=True)
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        data = Translation.objects.filter(source_language__in=['FR', 'EN'], target_language__in=['FR', 'EN'])  
        serialized_data = TranslationSerializer(data, many=True)
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
        
class AllTranslation(APIView):
    
    def get(self, request):
        data = Translation.objects.all()
        serialized_data =  TranslationSerializer(data, many=True)
        
        return Response(data=serialized_data.data, status=None)

def index(request):
    return render(request, 'index.html', context={})
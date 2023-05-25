from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
import language_tool_python
from .models import TextCorrection
from .serializers import TextCorrectionSerializer
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)


def index(request):
    return HttpResponse('Hello World')

class SpellcheckListview(ListCreateAPIView):
    queryset = TextCorrection.objects.all()
    serializer_class = TextCorrectionSerializer
    def post(self, request):
        original_text = request.data.get('original_txt')

        # Perform language correction
        tool = language_tool_python.LanguageToolPublicAPI('en-US')
        corrected_text = tool.correct(original_text)
        print(corrected_text)
        # Save the original and corrected texts in the database
        correction = TextCorrection.objects.create(
            original_txt=original_text,
            corrected_txt=corrected_text
        )

        # Serialize the text correction object
        serializer = TextCorrectionSerializer(correction)

        return Response(serializer.data)    

class SpellUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = TextCorrection.objects.all()
    serializer_class = TextCorrectionSerializer
    #permission_classes = [IsAuthenticated]
    # permission_classes = [Allow
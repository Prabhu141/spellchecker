from rest_framework import serializers
from .models import TextCorrection


class TextCorrectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextCorrection
        fields = ('id', 'original_txt', 'corrected_txt')
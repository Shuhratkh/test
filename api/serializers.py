from rest_framework import serializers
from query.models import Survey, Question

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['title', 'question', 'date_created', 'date_ended']
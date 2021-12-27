from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .serializers import SurveySerializer
from query.models import Survey, Question
class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    @action(detail=True,
            methods=['get'],
            serializer_class=SurveySerializer,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def surveys(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
class SurveyListView(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer





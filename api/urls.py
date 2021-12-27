from . import views
from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
router.register('surveys', views.SurveyViewSet)
app_name='query'
urlpatterns = [
    path('surveys/',views.SurveyListView.as_view(),name='survey_list'),
    path('', include(router.urls)),
]
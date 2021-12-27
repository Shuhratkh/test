from django.urls import path
from .views import Home, CreateSurvey, CreateQuestion, ListSurveys, EditSurveys, DeleteSurveys
urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('create/', CreateSurvey.as_view(), name='create'),
    path('create/question/', CreateQuestion.as_view(), name='createquestion'),
    path('surveys/', ListSurveys, name='surveys'),
    path('edit/<str:pk>/', EditSurveys.as_view(), name='edit'),
    path('delete/<str:pk>/', DeleteSurveys.as_view(), name='delete'),

]

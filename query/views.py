from django.shortcuts import render
from .models import Survey, Question
from django.views.generic import DeleteView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
class CreateQuestion(CreateView):
    model = Question
    template_name = 'createq.html'
    fields=['body', 'user']
class CreateSurvey(CreateView):
    model = Survey
    template_name = 'create.html'
    fields=['question', 'title', 'date_ended']
def ListSurveys(request):
    surveys=Survey.objects.all()
    context={"surveys":surveys}
    return render(request, 'surveys.html', context)
class EditSurveys(UpdateView):
    model=Survey
    template_name = 'edit_survey.html'
    fields=['question', 'title', 'date_ended']
class DeleteSurveys(DeleteView):
    model = Survey
    template_name = 'delete_survey.html'
    success_url = reverse_lazy('home')

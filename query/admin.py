from django.contrib import admin
from .models import Survey, Question, Answer
# Register your models here.
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Survey)

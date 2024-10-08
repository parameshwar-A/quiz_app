from django.shortcuts import render
import json
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'quiz_app/home.html')

def question_set(request, name):
    path = str(settings.BASE_DIR)+'/quiz_app/questions.json'
    print(path)
    with open(path, 'r') as file:
        questions = json.load(file)['questions'][:11]
    return render(request, 'quiz_app/questions.html', {'questions':questions})

    

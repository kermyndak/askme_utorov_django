from django.shortcuts import render
from django.core.paginator import Paginator

QUESTIONS = [
    {
        'id': i,
        'title': f"title {i}",
        'body': f"Question {i}"
    } for i in range(100)
]

ANSWERS = [
    {
        'correct': True if i == 0 else False, 
        'body': f'answer {i}'
    } for i in range(4)
]

def index(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS, per_page=5)
    page_obj = paginator.page(page_num)
    page_count = list(range(1, len([i for i in range(0, len(QUESTIONS), 5)]) + 1))
    return render(request, template_name='index.html', context={'questions': page_obj, 'page_range': page_count})

def hot(request):
    questions = QUESTIONS[::-1]
    return render(request, template_name='hot.html', context={'questions': questions})

def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, template_name='question.html', context={'question': item, 'answers': ANSWERS})

def login(request):
    return render(request, template_name='login.html')

def signup(request):
    return render(request, template_name='signup.html')

def ask(request):
    return render(request, template_name='ask.html')
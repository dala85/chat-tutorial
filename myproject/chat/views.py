from django.shortcuts import render
from django.http import HttpResponse
from .models import Chat


def home_view(request):
    chats = Chat.objects.all()

    if request.method == "POST":
        question = request.POST['question']
        answer = int(question) + 2

        Chat.objects.create(question=question, answer=answer)

    return render(request, 'home.html', {"chats": chats, 'name': 'Duncan'})

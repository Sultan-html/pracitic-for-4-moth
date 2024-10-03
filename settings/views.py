from django.shortcuts import render
# Create your views here.
def settings(requests):
    context = {
        'title': 'Главное'
    }
    return render(requests, 'index.html', context=context)
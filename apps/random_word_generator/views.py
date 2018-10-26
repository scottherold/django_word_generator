from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    random_str = get_random_string(length=14)
    if 'attempt' in request.session:
        request.session['attempt'] = int(request.session['attempt'] + 1)
    else:
        request.session['attempt'] = 1
    request.session['random_str'] = random_str
    return render(request, "random_word_generator/index.html")

def reset(request):
    if request.method == "POST":
        del request.session['attempt']
        return redirect("/")
    else:
        return redirect("/")
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import ContactForm

def home_page(request):
    context = {
        "title": "Hello World",
        "content": "Welcome to the homepage"
    }
    return render(request, "homepage.html", context)

def about_page(request):
    context = {
        "title": "About Page",
        "content": "Welcome to the about page"
    }
    return render(request, "homepage.html", context)

def contact_page(request):

    form = ContactForm(request.POST or None)

    context = {
        "title": "Contact Page",
        "content": "Welcome to the contact page",
        "form": form,
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "contact/view.html", context)


from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import JsonResponse, HttpResponse


def home_page(request):
    context = {
        "title": "Hello World",
        "content": "Welcome to the homepage",
        "premium": "You are logged in!"
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
        if request.is_ajax():
            return JsonResponse({"message": 'Thank you for your submission!'})

    if form.errors:
        errors = form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    return render(request, "contact/view.html", context)
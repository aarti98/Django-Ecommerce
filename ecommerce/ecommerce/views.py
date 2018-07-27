from django.shortcuts import render


def home_page(request):
    context = {
        "title": "Welcome",
        "content": "Welcome to the homepage",
        "premium": "You are logged in"
    }
    return render(request, "homepage.html", context)


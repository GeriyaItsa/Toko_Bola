from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406434172',
        'name': 'Muhammad Geriya Itsa',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
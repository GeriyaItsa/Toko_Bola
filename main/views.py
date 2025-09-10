from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'website' : 'Website toko bola',
        'name': 'Website ini milik Muhammad Geriya Itsa dengan NPM 2406434172',
    }

    return render(request, "main.html", context)
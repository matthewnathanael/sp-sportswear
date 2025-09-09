from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Matthew Nathanael',
        'class': 'PBP E',
        'aplikasi': 'SP Sportswear',
    }

    return render(request, "main.html", context)
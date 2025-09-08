from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Matthew Nathanael',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
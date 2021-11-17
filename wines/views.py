from django.shortcuts import render
from .models import Wine, Case

# Create your views here.


def all_wines(request):
    """ A view to show all wines, including sorting and search queries """

    wines = Wine.objects.all()

    context = {
        'wines': wines,
    }

    return render(request, 'wines/wines.html', context)


def all_cases(request):
    """ A view to show all wines, including sorting and search queries """

    cases = Case.objects.all()

    context = {
        'cases': cases,
    }

    return render(request, 'wines/cases.html', context)

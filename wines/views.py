from django.shortcuts import render, get_object_or_404
from .models import Wine, Case, Category
from django.db.models.functions import Lower

# Create your views here.


def all_wines(request):
    """ A view to show all wines, including sorting and search queries """

    wines = Wine.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                wines = wines.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            wines = wines.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            wines = wines.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    current_sorting = f'{sort}_{direction}'

    context = {
        'wines': wines,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'wines/wines.html', context)


def wine_detail(request, wine_id):
    """ A view to show indivdual wine details """

    wine = get_object_or_404(Wine, pk=wine_id)

    context = {
        'wine': wine,
    }

    return render(request, 'wines/wine_detail.html', context)


def all_cases(request):
    """ A view to show all cases, including sorting and search queries """

    cases = Case.objects.all()

    context = {
        'cases': cases,

    }

    return render(request, 'wines/cases.html', context)


def case_detail(request, case_id):
    """ A view to show indivdual case details """

    case = get_object_or_404(Case, pk=case_id)

    context = {
        'case': case,
    }

    return render(request, 'wines/case_detail.html', context)

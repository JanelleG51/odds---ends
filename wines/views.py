from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wine, Case, Category
from django.db.models.functions import Lower

from .forms import WineForm, CaseForm

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


@login_required
def add_wine(request):
    """ Add a wines to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permissions to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            wine = form.save()
            messages.success(request, 'Wine succesfully added!')
            return redirect(reverse('wine_detail', args=[wine.id]))
        else:
            messages.error(
                request, 'Failed to add wine. Please ensure the form is valid.')
    else:
        form = WineForm()

    template = 'wines/add_wine.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_case(request):
    """ Add a cases to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permissions to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            case = form.save()
            messages.success(request, 'Case succesfully added!')
            return redirect(reverse('case_detail', args=[case.id]))
        else:
            messages.error(
                request, 'Failed to add case. Please ensure the form is valid.')
    else:
        form = CaseForm()
    template = 'wines/add_case.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_case(request, case_id):
    """ Edit a case in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permissions to do that.')
        return redirect(reverse('home'))

    case = get_object_or_404(Case, pk=case_id)
    if request.method == 'POST':
        form = CaseForm(request.POST, request.FILES, instance=case)
        if form.is_valid():
            form.save()
            messages.success(request, 'Case successfully updated!')
            return redirect(reverse('case_detail', args=[case.id]))
        else:
            messages.error(
                request, 'Failed to update case. Please ensure the form is valid.')
    else:
        form = CaseForm(instance=case)
        messages.info(request, f'You are editing the {case.name} case')

    template = 'wines/edit_case.html'
    context = {
        'form': form,
        'case': case,
    }

    return render(request, template, context)


@login_required
def edit_wine(request, wine_id):
    """ Edit a wine in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permissions to do that.')
        return redirect(reverse('home'))

    wine = get_object_or_404(Wine, pk=wine_id)
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES, instance=wine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wine successfully updated!')
            return redirect(reverse('wine_detail', args=[wine.id]))
        else:
            messages.error(
                request, 'Failed to update wine. Please ensure the form is valid.')
    else:
        form = WineForm(instance=wine)
        messages.info(request, f'You are editing {wine.name}')

    template = 'wines/edit_wine.html'
    context = {
        'form': form,
        'wine': wine,
    }

    return render(request, template, context)


@login_required
def delete_wine(request, wine_id):
    """ Delete a wine from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permissions to do that.')
        return redirect(reverse('home'))

    wine = get_object_or_404(Wine, pk=wine_id)
    wine.delete()
    messages.success(request, 'Wine deleted!')
    return redirect(reverse('wines'))


@login_required
def delete_case(request, case_id):
    """ Delete a case from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permissions to do that.')
        return redirect(reverse('home'))

    case = get_object_or_404(Case, pk=case_id)
    case.delete()
    messages.success(request, 'Case deleted!')
    return redirect(reverse('cases'))

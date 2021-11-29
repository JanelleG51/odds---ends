from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from wines.models import Case

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, case_id):
    """ Add a quantity of the specified case to the shopping bag """

    case = get_object_or_404(Case, pk=case_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    type = None
    if 'case_type' in request.POST:
        type = request.POST['case_type']
    bag = request.session.get('bag', {})

    if type:
        if case_id in list(bag.keys()):
            if type in bag[case_id]['items_by_type'].keys():
                bag[case_id]['items_by_type'][type] += quantity
                messages.success(
                    request, f'Updated case {type.upper()} {case.name} quantity to {bag[case_id]["items_by_type"][type]}')
            else:
                bag[case_id]['items_by_type'][type] = quantity
        else:
            bag[case_id] = {'items_by_type': {type: quantity}}
            messages.success(
                request, f'Added {type.upper()} {case.name} to your bag')

    else:
        if case_id in list(bag.keys()):
            bag[case_id] += quantity
            messages.success(
                request, f'Updated {case.name} quantity to {bag[case_id]}')
        else:
            bag[case_id] = quantity
            messages.success(
                request, f'Added {case.name} case to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, case_id):
    """ Add the quantity of the specified case in the shopping bag """

    case = get_object_or_404(Case, pk=case_id)
    quantity = int(request.POST.get('quantity'))
    a_type = None
    if 'case_type' in request.POST:
        a_type = request.POST['case_type']
    bag = request.session.get('bag', {})

    if type:
        if quantity > 0:
            bag[case_id]['items_by_type'][a_type] = quantity
            messages.success(
                request, f'Updated {a_type.upper()} {case.name} case quantity to {bag[case_id]["items_by_type"][a_type]}')
        else:
            del bag[case_id]['items_by_type'][a_type]
            if not bag[case_id]['items_by_type']:
                bag.pop(case_id)
            messages.success(
                request, f'Removed {type.upper()} {case.name} from your bag')

    else:
        if quantity > 0:
            bag[case_id] += quantity
            messages.success(
                request, f'Updated {case.name} quantity to {bag[case_id]}')
        else:
            bag.pop(case_id)
            messages.success(
                request, f'Removed {case.name} case from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, case_id):
    """ Remove case from shopping bag """

    try:
        case = get_object_or_404(Case, pk=case_id)
        a_type = None
        if 'case_type' in request.POST:
            a_type = request.POST['case_type']
        bag = request.session.get('bag', {})

        if a_type:
            del bag[case_id]['items_by_type'][a_type]
            if not bag[case_id]['items_by_type']:
                bag.pop(case_id)
            messages.success(
                request, f'Removed {a_type.upper()} {case.name} from your bag')

        else:
            bag.pop(case_id)
            messages.success(
                request, f'Removed {case.name} case from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from wines.models import Case

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, case_id):
    """ Add a quantity of the specified case to the shopping bag """

    case = Case.objects.get(pk=case_id)
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
            else:
                bag[case_id]['items_by_type'][type] = quantity
        else:
            bag[case_id] = {'items_by_type': {type: quantity}}

    else:
        if case_id in list(bag.keys()):
            bag[case_id] += quantity
        else:
            bag[case_id] = quantity
            message.success(request, f'Added {case.name} case to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, case_id):
    """ Add the quantity of the specified case in the shopping bag """

    quantity = int(request.POST.get('quantity'))
    type = None
    if 'case_type' in request.POST:
        type = request.POST['case_type']
    bag = request.session.get('bag', {})

    if type:
        if quantity > 0:
            bag[case_id]['items_by_type'][type] = quantity
        else:
            del bag[case_id]['items_by_type'][type]
            if not bag[case_id]['items_by_type']:
                bag.pop(case_id)

    else:
        if quantity > 0:
            bag[case_id] += quantity
        else:
            bag.pop(case_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, case_id):
    """ Remove case from shopping bag """

    try:

        type = None
        if 'case_type' in request.POST:
            type = request.POST['case_type']
        bag = request.session.get('bag', {})

        if type:
            del bag[case_id]['items_by_type'][type]
            if not bag[case_id]['items_by_type']:
                bag.pop(case_id)

        else:
            bag.pop(case_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)

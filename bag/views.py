from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, case_id):
    """ Add a quantity of the specified product to the shopping bag """

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

    else:
        if quantity > 0:
            bag[case_id] += quantity
        else:
            bag.pop[case_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

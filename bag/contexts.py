from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from wines.models import Case


def bag_contents(request):

    bag_items = []
    total = 0
    case_count = 0
    bag = request.session.get('bag', {})

    for case_id, quantity in bag.items():
        case = get_object_or_404(Case, pk=case_id)
        total += quantity * case.price
        case_count += quantity
        bag_items.append({
            'case_id': case_id,
            'quantity': quantity,
            'case': case,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'case_count': case_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

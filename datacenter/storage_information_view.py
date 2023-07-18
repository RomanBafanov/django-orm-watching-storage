from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, is_visit_long
from django.shortcuts import render


def storage_information_view(request):
    visit = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for v in visit:
        tik_tak, x = get_duration(v)
        if is_visit_long(x) == True:
            strange = 'Да!'
        else:
            strange = 'Нет'
        non_closed_visits.append(
            {
                'who_entered': v.passcard,
                'entered_at': v.entered_at,
                'duration': tik_tak,
                'is_strange': strange,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

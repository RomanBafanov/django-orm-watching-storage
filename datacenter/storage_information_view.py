from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.duration_of_visits import *
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visit in visits:
        time_visit, date_visit = get_duration(visit)
        if is_visit_long(date_visit):
            strange = 'Да!'
        else:
            strange = 'Нет'
        non_closed_visits.append(
            {
                'who_entered': visits.passcard,
                'entered_at': visits.entered_at,
                'duration': time_visit,
                'is_strange': strange,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

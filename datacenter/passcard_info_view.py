from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.duration_of_visits import *
from django.shortcuts import render, get_object_or_404


this_passcard_visits = []

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        time_visit, date_visit = get_duration(visit)
        if is_visit_long(date_visit):
            strange = 'Да!'
        else:
            strange = 'Нет'
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': time_visit,
                'is_strange': strange,
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

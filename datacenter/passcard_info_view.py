from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, is_visit_long
from django.shortcuts import render, get_object_or_404


this_passcard_visits = []

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    # Программируем здесь
    visits = Visit.objects.filter(passcard=passcard)
    for v in visits:
        tik_tak, x = get_duration(v)
        if is_visit_long(x) == True:
            strange = 'Да!'
        else:
            strange = 'Нет'
        this_passcard_visits.append(
            {
                'entered_at': v.entered_at,
                'duration': tik_tak,
                'is_strange': strange,
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

from django.utils import timezone
import time


def is_visit_long(visit, minutes=60):
    if visit > minutes:
        return True
    return False


def get_duration(visit):
    if visit.leaved_at != None:
        t = visit.leaved_at - visit.entered_at
    else:
        t = timezone.now() - visit.entered_at
    time_visit = time.strftime("%H:%M:%S", time.gmtime(t.seconds))
    date_visit = t.seconds / 60

    return time_visit, date_visit
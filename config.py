import time
import pytz
import datetime
from consult.models import Consultation
from utils.schedule import unbookProfessional

def background():
    consultations = Consultation.objects.filter(consult_done=False)

    while True:
        time.sleep(30)
        now = datetime.datetime.now(tz=pytz.UTC)
        for consultation in consultations:
            consult_end_time = consultation.end_time

            # check if the duration for the consultation
            # is over
            if now >= consult_end_time:
                print("Time up")
                unbookProfessional(consultation)
                continue
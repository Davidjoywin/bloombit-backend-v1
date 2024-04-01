from account.models import UserProfile, Professional
from consult.models import Consultation


def unbookProfessional(user, consultation):
    consultation = Consultation.objects.get(id = consultation.id)
    professional = consultation.professional_assigned
    professional.booked = False
    professional.save()
    return "Professional unbooked"
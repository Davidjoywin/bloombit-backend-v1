from consult.models import Professional, Consultation


def unbookProfessional(consultation):
    consultation = Consultation.objects.get(id = consultation.id)
    professional = consultation.professional_assigned
    professional = Professional.objects.get(id=professional.id)
    professional.booked = False
    professional.save()
    consultation.consult_done = True
    consultation.save()
    return "Consultation done and Professional unbooked successfully"
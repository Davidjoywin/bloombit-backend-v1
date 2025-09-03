from django.urls import path

from .views import (
    CreateAllergyView, GetAllergyView, GetPatientAllergies, ListAllergiesView,
    CreateLabResultView, GetLabResultView, GetPatientLabResults, ListLabResultsView,
    CreateMedicationView, GetMedicationView, GetPatientMedications, ListMedicationsView,
    CreateClinicalNoteView, GetClinicalNoteView, GetPatientClinicalNotes, ListClinicalNotesView,
    CreateMedicalConditionView, GetMedicalConditionView, GetPatientMedicalConditions, ListMedicalConditionsView,
    AuthPatientVitals, GetPatientVital, CreatePatientVitals, CreatePatient, GetPatientView, GetPatientVitals, ListPatientsView
)


urlpatterns = [
    # Patient endpoints
    path('create', CreatePatient.as_view(), name='create-patient'),
    path('<int:id>', GetPatientView.as_view(), name='get-patient'),
    path('all', ListPatientsView.as_view(), name='list-patients'),

    # vitals endpoints
    path('vitals', AuthPatientVitals.as_view(), name='patient-vitals'),
    path('vitals/create', CreatePatientVitals.as_view(), name='create-patient-vitals'),
    path('vitals/<int:vital_id>', GetPatientVital.as_view(), name='get-patient-vital'),
    path('patient-vitals/<int:patient_id>', GetPatientVitals.as_view(), name='get-all-patient-vitals'),

    # Allergy endpoints
    path('allergies', ListAllergiesView.as_view(), name='list-allergies'),
    path('allergy/<int:id>', GetAllergyView.as_view(), name='get-allergy'),
    path('allergy/create', CreateAllergyView.as_view(), name='create-allergy'),
    path('patient-allergies/<int:patient_id>', GetPatientAllergies.as_view(), name='get-patient-allergy'),

    # Lab Result endpoints
    path('lab-result/create', CreateLabResultView.as_view(), name='create-lab-result'),
    path('lab-result/<int:id>', GetLabResultView.as_view(), name='get-lab-result'),
    path('lab-results', ListLabResultsView.as_view(), name='list-lab-results'),
    path('patient-lab-results/<int:patient_id>', GetPatientLabResults.as_view(), name='patient-lab-result'),

    # Medication endpoints
    path('medication/create', CreateMedicationView.as_view(), name='create-medication'),
    path('medication/<int:id>', GetMedicationView.as_view(), name='get-medication'),
    path('medications', ListMedicationsView.as_view(), name='list-medications'),
    path('patient-medications/<int:patient_id>', GetPatientMedications.as_view(), name='patient-medication'),

    # Medical Condition endpoints
    path('medical-condition/create', CreateMedicalConditionView.as_view(), name='create-medical-condition'),
    path('medical-condition/<int:id>', GetMedicalConditionView.as_view(), name='get-medical-condition'),
    path('medical-conditions', ListMedicalConditionsView.as_view(), name='list-medical-conditions'),
    path('patient-medical-conditions/<int:patient_id>', GetPatientMedicalConditions.as_view(), name='patient-medical-conditions'),

    # Clinical Note endpoints
    path('clinical-note/create', CreateClinicalNoteView.as_view(), name='create-clinical-note'),
    path('clinical-note/<int:id>', GetClinicalNoteView.as_view(), name='get-clinical-note'),
    path('clinical-notes', ListClinicalNotesView.as_view(), name='list-clinical-notes'),
    path('patient-clinical-notes/<int:patient_id>', GetPatientClinicalNotes.as_view(), name='patient-clinical-notes')
]
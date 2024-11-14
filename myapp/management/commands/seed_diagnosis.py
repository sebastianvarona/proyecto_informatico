# myapp/management/commands/seed_diagnosis.py
import random
from datetime import timedelta, date
from django.core.management.base import BaseCommand
from myapp.models import XRayDiagnosis  # Replace 'myapp' with your app name

class Command(BaseCommand):
    help = 'Seed database with 15 XRayDiagnosis records'

    def handle(self, *args, **kwargs):
        xray_types = ['Chest', 'Abdomen', 'Skull', 'Pelvis', 'Spine']
        radiologists = ['Dr. Smith', 'Dr. Johnson', 'Dr. Patel', 'Dr. Lee', 'Dr. Brown']
        severities = ['Mild', 'Moderate', 'Severe']
        
        def random_date(start, end):
            delta = end - start
            random_days = random.randint(0, delta.days)
            return start + timedelta(days=random_days)
        
        # Creating 15 records
        for i in range(15):
            XRayDiagnosis.objects.create(
                patient_name=f'Patient {i+1}',
                patient_age=random.randint(18, 80),
                patient_gender=random.choice(['Male', 'Female', 'Other']),
                xray_type=random.choice(xray_types),
                diagnosis_summary=f'Summary for diagnosis {i+1}',
                detailed_findings=f'Detailed findings for diagnosis {i+1}',
                date_of_diagnosis=random_date(date(2023, 1, 1), date(2024, 1, 1)),
                radiologist_name=random.choice(radiologists),
                comments=f'Comments for diagnosis {i+1}',
                severity=random.choice(severities)
            )
        self.stdout.write(self.style.SUCCESS("15 XRayDiagnosis records created successfully."))

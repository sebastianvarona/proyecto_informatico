from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('professional', 'Professional'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    cc = models.CharField(max_length=20, unique=True)  # Número de cédula
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='xrays_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='xrays_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


class MedicalRecord(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medical_records")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ficha médica {self.id} de {self.user.username}"


class MedicalVideo(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name="videos")
    video_file = models.FileField(upload_to='medical_videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video {self.id} para ficha {self.medical_record.id}"


class Diagnosis(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name="diagnoses")
    video = models.ForeignKey(MedicalVideo, on_delete=models.CASCADE,
                              related_name="diagnoses", null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnóstico {self.id} para ficha {self.medical_record.id}"


class ProblemReport(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="problem_reports")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Reporte de problema {self.id} de {self.user.username}"


class PregnancyTracking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pregnancy_tracking")
    symptom = models.CharField(max_length=255)
    additional_details = models.TextField(blank=True)
    week_of_pregnancy = models.PositiveIntegerField()
    weight = models.FloatField(null=True, blank=True)
    blood_pressure = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Seguimiento del embarazo {self.id} de {self.user.username}"


class MedicalReminder(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medical_reminders")
    reminder_type = models.CharField(
        max_length=50)  # 'Vitaminas' o 'Cita Médica'
    reminder_time = models.DateTimeField()
    notification_method = models.CharField(max_length=50)  # Push, email, etc.

    def __str__(self):
        return f"Recordatorio {self.reminder_type} para {self.user.username}"


admin.site.register(User)
admin.site.register(MedicalRecord)
admin.site.register(MedicalVideo)
admin.site.register(Diagnosis)
admin.site.register(ProblemReport)
admin.site.register(PregnancyTracking)
admin.site.register(MedicalReminder)

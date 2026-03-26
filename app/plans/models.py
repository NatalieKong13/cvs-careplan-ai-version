from django.db import models

class CarePlan(models.Model):
    patient_name = models.CharField(max_length=200)
    age = models.IntegerField()
    diagnosis = models.TextField()
    medications = models.TextField()
    notes = models.TextField(blank=True)
    generated_plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

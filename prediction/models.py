from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PredictionSave(models.Model):
     user = models.ForeignKey(
         User, on_delete=models.CASCADE,
         null =True,
         blank=True)
     age = models.IntegerField()
     sex = models.CharField(max_length=1)
     chest_pain = models.CharField(max_length=15)
     resting_bp = models.IntegerField()
     cholesterol = models.IntegerField()
     fasting_bs = models.IntegerField()
     resting_ecg = models.CharField(max_length=10)
     max_hr =  models.IntegerField()
     oldpeak = models.FloatField()
     exercise_angina = models.CharField(max_length=1)
     st_slope = models.CharField(max_length=15)


     prediction = models.IntegerField()
     chance = models.FloatField()

     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return f"Prediction {self.id}"

from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50, blank=True)

class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    measurements = models.ForeignKey(Sensor, related_name='data_m', on_delete=models.CASCADE, blank=False, null=False,)

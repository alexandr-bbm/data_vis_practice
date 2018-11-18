from django.db import models

class MeasureDate(models.Model):
    value = models.DateField()

class Longitude(models.Model):
    value = models.FloatField()

class Latitude(models.Model):
    value = models.FloatField()

class Temperature(models.Model):
    value = models.FloatField()
    date = models.ForeignKey(MeasureDate, on_delete=models.CASCADE)
    lon = models.ForeignKey(Longitude, on_delete=models.CASCADE)
    lat = models.ForeignKey(Latitude, on_delete=models.CASCADE)


from django.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=100)
    id = models.SmallIntegerField(primary_key=True)
    start_snow_water_eq = models.FloatField()
    change_snow_water_eq = models.FloatField()
    start_snow_depth = models.FloatField()
    change_snow_depth = models.FloatField()
    
    def __str__(self):
        return self.name
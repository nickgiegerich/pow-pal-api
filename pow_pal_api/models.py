from django.db import models

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=100)
    state_id = models.CharField(primary_key=True, max_length=5)

class Station(models.Model):
    state = models.ForeignKey(State, related_name='stations', on_delete=models.CASCADE, default='WA')
    name = models.CharField(max_length=100)
    id = models.SmallIntegerField(primary_key=True)
    start_snow_water_eq = models.FloatField()
    change_snow_water_eq = models.FloatField()
    start_snow_depth = models.FloatField()
    change_snow_depth = models.FloatField()
    
    def __str__(self):
        return '%s %d' % (self.name, self.id)


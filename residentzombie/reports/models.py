from django.db import models

class Report(models.Model):

    infected_percent = models.FloatField(default=0.0)
    non_infected_percent = models.FloatField(default=0.0)
    water_avg = models.FloatField(default=0.0)
    soup_avg = models.FloatField(default=0.0)
    aid_pouch_avg = models.FloatField(default=0.0)
    ak47_avg = models.FloatField(default=0.0)
    lost_points = models.IntegerField(default=0.0)

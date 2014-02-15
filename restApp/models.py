from django.db import models

CITY_CHOICES = [('bogota','BOGOTA'),('cali','CALI'),('medellin','MEDELLIN')]

class Poll(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    city = models.CharField(choices=CITY_CHOICES,
                                default='bogota',
                                max_length=100)

    class Meta:
        ordering = ('created',)
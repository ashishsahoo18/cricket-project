from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    test_matches = models.IntegerField(default=0)
    odi_matches = models.IntegerField(default=0)
    t20_matches = models.IntegerField(default=0)

    test_runs = models.IntegerField(default=0)
    odi_runs = models.IntegerField(default=0)
    t20_runs = models.IntegerField(default=0)


    image = models.ImageField(upload_to='players/', blank=True)


    def __str__(self):
        return self.name
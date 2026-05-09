from django.db import models
class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='players/', blank=True)

    def __str__(self):
        return self.name


class PlayerStats(models.Model):
    FORMAT_CHOICES = [
        ('TEST', 'Test'),
        ('ODI', 'ODI'),
        ('T20', 'T20'),
        ('IPL', 'IPL'),
    ]

    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="stats")
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)

    matches = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    high_score = models.IntegerField(default=0)

    average = models.FloatField(default=0)
    strike_rate = models.FloatField(default=0)

    hundreds = models.IntegerField(default=0)
    fifties = models.IntegerField(default=0)

    

    class Meta:
        unique_together = ("player", "format")

    def __str__(self):
        return f"{self.player.name} - {self.format}"
from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.CharField(max_length=500)
    verified_artist = models.BooleanField(default=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self): #fa vedere su admin il nome e non un dato strano
        return "Artist: " + self.name

    # Assicira che i dati vengano visializzati in ordine alfabetico per nome
    class Meta:
        ordering = ['name']

from django.db import models

# Create your models here.
class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.URLField()
    
    def __str__(self):
        return self.title


class Chart(models.Model):
    chart_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    views = models.IntegerField()
    films = models.ManyToManyField(Film, through='FilmChart')
    
    def __str__(self):
        return self.title

class FilmChart(models.Model):
    """
    :param: film - Film foreign key
    :param: chart - Chart foreign key
    """
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Film')
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE, verbose_name='Chart')
    #description = models.TextField()


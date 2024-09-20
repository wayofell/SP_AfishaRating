from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Директоры'
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text='В минутах')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    stars = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'Review for {self.movie.title} with rating {self.stars}'


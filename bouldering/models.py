from django.db import models
from django.contrib.auth.models import User

class WallSection(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    image = models.ImageField(upload_to='pics')

class Route(models.Model):
    wall_section = models.ForeignKey(WallSection, on_delete=models.CASCADE)
    colour = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)
    users = models.ManyToManyField(User)

    def __str__(self):
        return "%s %d" % (self.colour, self.grade)

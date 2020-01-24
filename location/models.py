from django.db import models


class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class LGA(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__self(self):
        return self.name


class City(models.Model):
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.lga, self.name)

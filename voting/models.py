from django.db import models
from accounts.model import Account


class Position(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contestant(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Account)


class Election(models.Model):
    title = models.CharField(max_length=100)
    contestants = models.ForeignKey(Contestant)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Voting(models.Models):
    voter = models.ForeignKey(Account)
    count = models.PositiveIntegerField(default=0)
    pass

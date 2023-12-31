from django.db import models


class RegisterPermission(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "Status = {}".format(self.status)

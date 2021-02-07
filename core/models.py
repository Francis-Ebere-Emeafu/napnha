from django.db import models


class RegisterPermission(models.Model):
    status = models.BooleanField(default=False)

    def __str__(self):
        return "Status = {}".format(self.status)

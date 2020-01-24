from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime


class Account(models.Model):
    FEMALE = 0
    MALE = 1
    SEX = enumerate(('Female', 'Male'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    alt_phone = models.CharField(max_length=20)
    state_code = models.CharField(max_length=30)
    call_up_num = models.CharField(max_length=30)
    gender = models.PositiveIntegerField(choices=SEX, null=True, blank=True)
    dob = models.DateField(verbose_name='Date of birth', null=True, blank=True)
    registered_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

    @property
    def age(self):
        if self.dob:
            return int((datetime.now().date() - self.dob).days / 365.25)
        else:
            return str("No age")


class Profile(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    ministry = models.CharField(max_length=200, blank=True)
    level = models.CharField(max_length=200, blank=True)

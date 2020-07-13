from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime

from hashid_field import HashidAutoField

class Account(models.Model):
    FEMALE = 0
    MALE = 1
    SEX = enumerate(('Female', 'Male'))

    # id = HashidAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    whatsapp_phone = models.CharField(max_length=20, null=True, blank=True)
    state_code = models.CharField(max_length=30, null=True, blank=True)
    call_up_num = models.CharField(max_length=30, null=True, blank=True)
    state_of_origin = models.CharField(max_length=30, null=True, blank=True)
    lga_of_origin = models.CharField(max_length=30, null=True, blank=True)
    gender = models.PositiveIntegerField(choices=SEX, null=True, blank=True)
    dob = models.DateField(verbose_name='Date of birth', null=True, blank=True)
    profession = models.CharField(max_length=200, blank=True, null=True)
    ministry = models.CharField(max_length=200, blank=True, null=True)
    level = models.CharField(max_length=200, blank=True)
    office_address = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to="profile", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    confirm_email = models.BooleanField(default=False)
    napnha_number = models.PositiveIntegerField(null=True, blank=True)
    certificate = models.ImageField(upload_to='certificates', null=True, blank=True)
    next_payment_due = models.DateField(null=True, blank=True)
    
    registered_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}, {}".format(self.surname, self.first_name)

    @property
    def age(self):
        if self.dob:
            return int((datetime.now().date() - self.dob).days / 365.25)
        else:
            return str("No age")


class Renewal(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_date = models.DateField()

    def __unicode__(self):
        return unicode(self.account)
    

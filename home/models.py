# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Paymentconfig(models.Model):

    #__Paymentconfig_FIELDS__
    secret = models.TextField(max_length=255, null=True, blank=True)
    consumer = models.TextField(max_length=255, null=True, blank=True)
    passkey = models.TextField(max_length=255, null=True, blank=True)
    shortcode = models.TextField(max_length=255, null=True, blank=True)
    callbackurl = models.TextField(max_length=255, null=True, blank=True)
    validationurl = models.TextField(max_length=255, null=True, blank=True)
    identifier = models.TextField(max_length=255, null=True, blank=True)
    payurl = models.TextField(max_length=255, null=True, blank=True)

    #__Paymentconfig_FIELDS__END

    class Meta:
        verbose_name        = _("Paymentconfig")
        verbose_name_plural = _("Paymentconfig")


class Station(models.Model):

    #__Station_FIELDS__
    code = models.TextField(max_length=255, null=True, blank=True)

    #__Station_FIELDS__END

    class Meta:
        verbose_name        = _("Station")
        verbose_name_plural = _("Station")


class Payment(models.Model):

    #__Payment_FIELDS__
    transid = models.TextField(max_length=255, null=True, blank=True)
    shortcode = models.TextField(max_length=255, null=True, blank=True)
    billrefnumber = models.TextField(max_length=255, null=True, blank=True)
    msisdn = models.TextField(max_length=255, null=True, blank=True)
    firstname = models.TextField(max_length=255, null=True, blank=True)
    transactiontype = models.TextField(max_length=255, null=True, blank=True)
    transtime = models.TextField(max_length=255, null=True, blank=True)
    invoicenumber = models.TextField(max_length=255, null=True, blank=True)

    #__Payment_FIELDS__END

    class Meta:
        verbose_name        = _("Payment")
        verbose_name_plural = _("Payment")


class Device(models.Model):

    #__Device_FIELDS__
    deviceidentifier = models.TextField(max_length=255, null=True, blank=True)
    language = models.TextField(max_length=255, null=True, blank=True)
    identifier = models.TextField(max_length=255, null=True, blank=True)

    #__Device_FIELDS__END

    class Meta:
        verbose_name        = _("Device")
        verbose_name_plural = _("Device")


class Ticket(models.Model):

    #__Ticket_FIELDS__
    vtype = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)

    #__Ticket_FIELDS__END

    class Meta:
        verbose_name        = _("Ticket")
        verbose_name_plural = _("Ticket")


class Categoryrate(models.Model):

    #__Categoryrate_FIELDS__
    amount = models.TextField(max_length=255, null=True, blank=True)
    hoursfrom = models.TextField(max_length=255, null=True, blank=True)
    hoursto = models.TextField(max_length=255, null=True, blank=True)

    #__Categoryrate_FIELDS__END

    class Meta:
        verbose_name        = _("Categoryrate")
        verbose_name_plural = _("Categoryrate")


class Vehiclecategory(models.Model):

    #__Vehiclecategory_FIELDS__
    status = models.TextField(max_length=255, null=True, blank=True)

    #__Vehiclecategory_FIELDS__END

    class Meta:
        verbose_name        = _("Vehiclecategory")
        verbose_name_plural = _("Vehiclecategory")



#__MODELS__END

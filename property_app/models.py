from django.db import models

from django.contrib.auth.models import User


class Property(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField()
    number_of_units = models.IntegerField()

    def __str__(self):
        return self.name


class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.IntegerField()
    bedrooms = models.IntegerField()
    rent = models.IntegerField()
    is_available = models.BooleanField(default=True)


class Tenant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.IntegerField()

    def __str__(self):
        return self.tenant

# Create your models here.

from django.db import models

class Company(models.Model):
    COMPANY_PIN = models.CharField(max_length=100)
    COMPANY_NAME = models.CharField(max_length=200)
    ITAX_STATUS = models.CharField(max_length=100)
    COMPANY_REG_STATUS = models.CharField(max_length=100)
    PHYSICAL_LOCATION = models.TextField()
    POSTAL_ADDRESS = models.TextField()
    COMPANY_CONTACT = models.CharField(max_length=100)
    BUSINESS_REG_NUM = models.CharField(max_length=100)
    EMAIL_ADDRESS = models.EmailField()

    def __str__(self):
        return self.COMPANY_NAME

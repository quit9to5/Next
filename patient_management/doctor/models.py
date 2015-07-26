from django.db import models

# Create your models here.

class doctor(models.Model):
    email = models.EmailField()
    full_name = models.CharField(blank=True, null=True, max_length=120)
    mobile_number = models.CharField(blank=True, null=True, max_length=13)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email

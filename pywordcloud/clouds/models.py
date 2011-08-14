from django.db import models

class Cloud(models.Model):
    cloud_id = models.BigIntegerField (primary_key = True)
    name = models.CharField (max_length = 200)
    text = models.TextField (blank = True)
    datetime_created = models.DateTimeField ('date of creation')
    datetime_updated = models.DateTimeField ('last updated')
    image = models.ImageField (max_length = 500, blank = True, upload_to = 'images/')
    ip_address = models.IPAddressField (blank = True)

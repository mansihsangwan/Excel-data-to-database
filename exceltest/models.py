from django.db import models


class TrainerDetails(models.Model):
    first_name    = models.CharField(max_length = 100)
    last_name     = models.CharField(max_length = 100)
    mobile_number = models.CharField(max_length = 100)
    location      = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name
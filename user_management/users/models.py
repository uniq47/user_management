from django.db import models

class User(models.Model):
    STATUS_CHOICES = (
        ('I', 'Inactive'),
        ('A', 'Active'),
        ('T', 'Terminated'),
    )

    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    user_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    department = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user_name

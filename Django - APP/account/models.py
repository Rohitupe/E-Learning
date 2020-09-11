from django.db import models

# Create your models here.
class Account_info(models.Model):
    first_name = models.CharField(max_length = 500)
    last_name = models.CharField(max_length = 500)
    email = models.EmailField()
    password = models.CharField(max_length = 500)
    paid_user = models.BooleanField(default=False)
    login_info = models.DateTimeField()

    def __str__(self):
        return self.first_name + " " + self.last_name
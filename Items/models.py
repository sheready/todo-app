from django.db import models

# Create your models here.
class Items(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    deadline = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.title


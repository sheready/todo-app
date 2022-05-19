from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image
# Create your models here.

class Person(AbstractUser):
    phone =models.TextField(max_length=20, blank=False)
    is_verified = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='images/Avatar.png', upload_to='images')
    

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

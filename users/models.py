from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #if the user is deleted it will also delete the profile, if we delete the profile it won't delete the user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # def save(self, **kwargs):
    #     super().save(**kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width >300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)



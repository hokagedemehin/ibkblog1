from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # we can have auto_now=True or auto_now_add=True
    author = models.ForeignKey(User, on_delete=models.CASCADE) # one user can have many posts but only one post can be associated with one user, hence a one to many relationship between post and user model
                                                                # models.CASCADE will delete all the post associated with a user if the user is deleted, if post is deleted, nothing will happen to the user
                                                                # models.SET_NULL and null=True will not delete the post associated with a user that is deleted
                                                                # python manage.py sqlmigrate blog "0001 - remember this at the beginning of the py file in migrtions folder" - This shows the sql code that will create a table that we just did a makemigrations on
                                                                # python manage.py shell
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
                                                    

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    portfoliosite = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self) -> str:
        return self.user.username
from django.db import models
from api.models import Images
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User,  related_name='profile', on_delete=models.CASCADE)
    country = CountryField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image = models.ForeignKey(Images, on_delete=models.CASCADE, null=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):

    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICE = (
        (CREATOR, 'Creator'),
        (SUBSCRIBER, 'Subscriber'),
    )

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creators')
            group.user_set.add(self)

        if self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)



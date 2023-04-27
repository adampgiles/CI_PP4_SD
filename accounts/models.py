from django.db import models
from django.contrib.auth.models import User
from developers.models import Developer


class UserAccount(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,
                                on_delete=models.SET_NULL)
    is_developer = models.BooleanField(default=False)
    purchased_developers = models.ManyToManyField(Developer, blank=True)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactUs(models.Model):

    class Meta:
        verbose_name_plural = "ContactUs"

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=254)
    body = models.TextField(max_length=500)
    sent_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.subject
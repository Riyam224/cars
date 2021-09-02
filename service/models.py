from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify



COLOR_CHOICES = (
    ('W' , 'White'),
    ('O' , 'Others')
)


SERVICES_CHOICES = (
    ('CL' , 'Clean'),
    ('WA' , 'Wash'),
    ('Ad' , 'Add Oil')
)
class Car(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)
    color = models.CharField(choices=COLOR_CHOICES , max_length=1)
    image = models.ImageField(upload_to='cars', blank=True)
    service =  models.CharField(choices=SERVICES_CHOICES , max_length=2)
    desc = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

    def __str__(self):
        return self.name





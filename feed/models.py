from django.db import models
from django.forms import ImageField
from sorl.thumbnail import ImageField   

class Post(models.Model):
    text = models.CharField(max_length=150, blank=False, null=False)
    date = models.DateTimeField(auto_now=True)
    image = ImageField()

    def __str__(self):
        return self.text
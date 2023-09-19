from django.db import models
from random import randint, choice
from string import ascii_lowercase


class Image(models.Model):
    title = ''.join([choice(ascii_lowercase) for i in range(10)]) + str(randint(100, 1000))
    # name = models.CharField(name='Кличка', max_length=100)
    # breed = models.CharField(name='Порода', max_length=100)
    # age = models.IntegerField(name='Возраст', max_length=100)
    # color = models.CharField(name='Окрас', max_length=100)
    # food = models.CharField(name='Корм', max_length=100)
    img = models.ImageField(upload_to='static/img/pet_images')

    def __str__(self):
        return self.title

from django.db import models
from django.shortcuts import reverse


class Presets(models.Model):
    img = models.ImageField(upload_to="presets/")
    description = models.TextField()
    bold_description = models.TextField()
    lot = models.CharField(max_length=255)
    rating = models.IntegerField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    buy_href = models.CharField(max_length=1000)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_link(self):
        return reverse('preset', args=[self.slug])


class PresetsExamples(models.Model):
    preset = models.OneToOneField(Presets, on_delete=models.CASCADE)

    before = models.ImageField()
    after = models.ImageField()

    def __str__(self):
        return f'{self.preset}'


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    who_is_you = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.who_is_you}'


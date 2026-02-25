from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Hobbies(models.Model):
    hobby_name = models.CharField(max_length=100)
    hobby_description = models.CharField(max_length=400)
    hobby_img = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return f"{self.hobby_name}: {self.hobby_description}"


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField(default='fallback.png', blank=True)
    link = models.URLField(max_length=500, default="https://github.com/ethanMinson?tab=repositories")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}: {self.description}"

class Contact(models.Model):
    name = models.CharField(max_length=100, validators=[RegexValidator(
        regex='^[a-zA-Z ]*$',
        message='Name must be alpha characters only',
        code='invalid_name'
    )])
    email = models.EmailField(max_length=100, validators=[EmailValidator(
        message='Email must be valid',
        code='invalid_email'
    )])
    message = models.TextField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"{self.name}: {self.email}"
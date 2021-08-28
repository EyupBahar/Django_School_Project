from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name


class Teacher(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='teacher', default="default.jpg")
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)

    TITLE = (
        ('English', 'English Teacher'),
        ('Scratch', 'Scratch Teacher'),
        ('Science', 'Science Teacher'),
        ('Sport', 'Sport Teacher'),
    )

    speciality = models.CharField(max_length=50, choices=TITLE)

    def __str__(self):
        return self.name
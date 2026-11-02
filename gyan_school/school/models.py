
from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(
        max_length=100,
        default='Discover Our School'
    )
    button_link = models.CharField(
        max_length=200,
        default='#about'
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class SchoolInfo(models.Model):
    title = models.CharField(
        max_length=200,
        default='About Gyan School'
    )
    description = models.TextField()
    image = models.ImageField(upload_to='school/')
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.title


class SchoolClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='classes/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(
        max_length=100,
        default='bi bi-book'
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ContactEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'

from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


#team members
class TeamMember(models.Model):
    name = models.CharField(max_length=64, verbose_name='Name of Team member')
    title = models.CharField(max_length=64, verbose_name="Position")
    about = models.TextField(verbose_name="About You")
    image = models.ImageField(verbose_name="Profile image")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"


#products
class Product(models.Model):
    product_type = {
        ('BOOK', "Available"),
        ('CUP', "Cup"),
        ('BAND', "Wrist band"),
        ('TSHIRT', "T-shirt"),

    }
    name = models.CharField(max_length=128, verbose_name="Name of Product")
    quantity = models.IntegerField(verbose_name="Quantity available")
    price = models.IntegerField(verbose_name="Price")
    type_of_product = models.CharField(verbose_name="Product Type", choices=product_type, max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


#about amazing quotes
class AmazingQuotesAbout(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(verbose_name="About Amazing Quotes")
    phone_no = models.CharField(max_length=20, default='0712626160')
    email = models.EmailField(default='amazingquotes@gmail.com')
    facebook = models.URLField(max_length=128, default='https://facebook.com/amazingquotes',
                                verbose_name='Facebook link')
    instagram = models.URLField(max_length=128, default='https://insta.com/amazingquotes',
                                verbose_name='Instagram link')
    twitter = models.URLField(max_length=128, default='https://twitter.com/amazingquotes',
                                verbose_name='Twitter link')
    linkedin = models.CharField(max_length=128, default='https://linkedin.com/amazingquotes',
                                verbose_name='Linkedin link')
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if AmazingQuotesAbout.objects.exists() and not self.pk:
            raise ValidationError('There is can be only one Amazing Quote instance')
        return super(AmazingQuotesAbout, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "About Amazing Quotes"
        verbose_name_plural= "About Amazing Quotes"


#events
class Event(models.Model):
    name = models.CharField(max_length=128)
    type_of_event = models.CharField(max_length=128)
    time = models.DateTimeField(verbose_name="Date and Time")
    city = models.CharField(max_length=128, verbose_name="City")
    location = models.CharField(max_length=64, verbose_name="Location")
    price = models.IntegerField(verbose_name="Price (0 if free)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = "Events"


#gallery
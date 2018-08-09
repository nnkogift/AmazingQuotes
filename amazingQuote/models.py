from django.core.exceptions import ValidationError
from django.db import models
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()
# Create your models here.


# team members
class TeamMember(models.Model):
    speaking = {
        ('YES', 'Yes'),
        ('NO', 'No')
    }

    name = models.CharField(max_length=64, verbose_name='Name of Team member')
    title = models.CharField(max_length=64, verbose_name="Position")
    about = models.TextField(verbose_name="About You")
    image = models.ImageField(verbose_name="Profile image", upload_to='team', storage=gd_storage)
    email = models.EmailField(verbose_name='Email', default='amazingquotes@gmail.com')
    phone_no = models.CharField(max_length=15, default='+255712626160')
    speaker = models.CharField(max_length=5, choices=speaking, default='NO')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"


#products
class Product(models.Model):
    product_type = {
        ('BOOK', "Book"),
        ('CUP', "Cup"),
        ('BAND', "Wrist band"),
        ('TSHIRT', "T-shirt"),

    }
    featured = {
        ('YES', "Yes"),
        ('NO', "No")
    }
    name = models.CharField(max_length=128, verbose_name="Name of Product")
    quantity = models.IntegerField(verbose_name="Quantity available")
    price = models.IntegerField(verbose_name="Price")
    type_of_product = models.CharField(verbose_name="Product Type", choices=product_type, max_length=64)
    feature = models.CharField(verbose_name='Is it Featured?', default='YES', choices=featured, max_length=10)

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
    address = models.CharField(max_length=128, verbose_name='Address', default='Dar es Salaam')
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
    price = models.IntegerField(verbose_name="Price (0 if free)", default=0)
    description = models.TextField(verbose_name="About event", default='This is one of our'
                                                                       ' events you will never forget.')
    video_url = models.URLField(verbose_name="Video", default='https://www.youtube.com/watch?v=SQVpx1LFloI&t=79s', blank=True)
    image = models.ImageField(default='media/Albert-Einstein-Quote-About-Life-Wallpaper.png', verbose_name='Event Poster', upload_to='events', storage=gd_storage)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = "Events"


class EventRegistration(models.Model):
    name_of_event = models.ForeignKey(Event, related_name='registrar', on_delete=models.CASCADE)
    name_of_registrar = models.CharField(max_length=128, default='Attendee')
    email_of_registrar = models.EmailField()
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.name_of_registrar

    class Meta:
        verbose_name_plural="Registered Attendees"
        verbose_name="Registered Attendee"

#gallery


# contacts
class ContactRequests(models.Model):
    name = models.CharField(max_length=64, verbose_name="From")
    email = models.EmailField(verbose_name='Email')
    phoneno = models.CharField(max_length=15, verbose_name="Phone Number")
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Requests"
        verbose_name = "Contact Request"


class Value(models.Model):
    about = models.ForeignKey(AmazingQuotesAbout, related_name='values', on_delete=models.CASCADE)
    value = models.CharField(max_length=128, default='Value')
    description = models.TextField(verbose_name="Value Description", max_length=256)


class Order(models.Model):
    product = models.ForeignKey(Product, related_name='order', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=128, verbose_name="Name of The person Ordering")
    email = models.EmailField()
    phone_no = models.CharField(max_length=15, verbose_name="Phone number")


class Quote(models.Model):
    content = models.TextField(verbose_name='The quote')
    writer = models.CharField(verbose_name='Quote by', max_length=64)
    quote_image = models.ImageField(verbose_name='Quote Image', upload_to='quotes', storage=gd_storage)
    date_of_publish = models.DateField(verbose_name='Date to be published', unique=True, auto_created=False,
                                       auto_now=False)

    def __str__(self):
        return self.writer

    class Meta:
        verbose_name='Quote of the Day'
        verbose_name_plural = 'Daily quotes'


class TrainingTopic(models.Model):
    post_category = {
        ('RELATIONSHIP', 'Relationship'),
        ('LIFE COACHING', 'Life Coaching'),
        ('LEADERSHIP', 'Leadership'),
        ('ENTREPRENEURSHIP', 'Entrepreneurship')
    }
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=20, choices=post_category, default='LIFE COACHING')
    description = models.TextField()
    speaker = models.ForeignKey(TeamMember, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

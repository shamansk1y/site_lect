from django.db import models
from django.core.validators import RegexValidator
import os
import uuid

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Категорії'
        verbose_name = 'Категорія'

    def __iter__(self):
        for item in self.dishes.all():
            yield item

class Dish(models.Model):

    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('media/dishes/', new_file_name)

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.TextField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position')
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'

class Team(models.Model):

    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('media/team/', new_file_name)

    name_staff = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    profession = models.TextField(max_length=255)
    staff_photo = models.ImageField(upload_to=get_file_name, blank=True)
    img_twitter = models.ImageField(upload_to=get_file_name, blank=True)
    img_fb = models.ImageField(upload_to=get_file_name, blank=True)
    img_insta = models.ImageField(upload_to=get_file_name, blank=True)
    img_in = models.ImageField(upload_to=get_file_name, blank=True)

    def __str__(self):
        return f'{self.name_staff}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Наша команда'

class Galery(models.Model):

    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('media/galery/', new_file_name)

    title = models.CharField(max_length=50, unique=True, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Галерея'

class Booking(models.Model):

    book_num = models.SmallIntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=50, help_text='Your name')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    num_of_pers = models.SmallIntegerField()
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.book_num}: {self.date} {self.time}'

    class Meta:
        ordering = ('book_num', 'date')
        verbose_name = 'Book'
        verbose_name_plural = 'Тест Бронювання'

class Events(models.Model):

    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('media/events/', new_file_name)

    title = models.CharField(max_length=50, unique=True, db_index=True)
    event_date = models.DateTimeField()
    photo = models.ImageField(upload_to='get_file_name')
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    desc = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('event_date', 'price')
        verbose_name = 'Event'
        verbose_name_plural = 'Заходи'

class About(models.Model):

    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('media/about/', new_file_name)

    h_1 = models.CharField(max_length=255, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    desc = models.TextField(max_length=500)
    url_video = models.URLField()

    def __str__(self):
        return f'{self.h_1}'

    class Meta:
        verbose_name_plural = 'Про нас'


class Reservation(models.Model):
    phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[ -]?){7}$', message='Error phone number')

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    persons = models.SmallIntegerField()
    message = models.TextField(max_length=250, blank=True)

    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.phone}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Бронювання'

class WhyUs(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    desc = models.TextField(max_length=255)

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Чому нас'



class Slider(models.Model):

    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('media/slider/', new_file_name)


    title = models.CharField(max_length=50)
    position = models.SmallIntegerField(unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    h_1 = models.CharField(max_length=250, blank=True)
    desc = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Слайдер'


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject_mes = models.CharField(max_length=50)
    message = models.TextField(max_length=250, blank=True)

    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Повідомлення'

class ContactInfo(models.Model):
    location = models.CharField(max_length=50)
    location_text = models.CharField(max_length=50)
    open_hours = models.CharField(max_length=50)
    open_hours_text = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    email_text = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    phone_text = models.CharField(max_length=50)
    desc = models.TextField(max_length=250)
    h1 = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Контактна інформація'

class Footer(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    twitter = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    google_plus = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Футер'


class Testimonials(models.Model):

    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('media/testimonials/', new_file_name)

    photo = models.ImageField(upload_to=get_file_name)
    name = models.CharField(max_length=50)
    prof = models.CharField(max_length=50)
    star = models.SmallIntegerField(blank=True)
    text = models.TextField(max_length=250)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Відгуки'



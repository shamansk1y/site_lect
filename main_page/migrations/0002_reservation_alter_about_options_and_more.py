# Generated by Django 4.1.5 on 2023-02-09 17:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='', regex='')])),
                ('persons', models.SmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_processing', models.DateField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'Про нас'},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ('book_num', 'date'), 'verbose_name': 'Book', 'verbose_name_plural': 'Тест Бронювання'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('position',), 'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('category', 'position'), 'verbose_name': 'Страва', 'verbose_name_plural': 'Страви'},
        ),
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ('position', 'price'), 'verbose_name': 'Event', 'verbose_name_plural': 'Заходи'},
        ),
        migrations.AlterModelOptions(
            name='galery',
            options={'ordering': ('position',), 'verbose_name_plural': 'Галерея'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('position',), 'verbose_name_plural': 'Наша команда'},
        ),
    ]

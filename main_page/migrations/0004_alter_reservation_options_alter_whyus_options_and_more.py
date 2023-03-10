# Generated by Django 4.1.5 on 2023-02-09 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_whyus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ('-date',), 'verbose_name_plural': 'Бронювання'},
        ),
        migrations.AlterModelOptions(
            name='whyus',
            options={'ordering': ('position',), 'verbose_name_plural': 'Чому нас'},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Input phone № in format xxx xxx xxxx', regex='^(\\d{3}[- .]?){2}\\d{4}$')]),
        ),
    ]

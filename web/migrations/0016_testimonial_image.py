# Generated by Django 4.2.6 on 2023-10-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_rename_coverletter_testimonial_paragraph'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(default='upload', upload_to='testimonial'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='profiles'),
            preserve_default=False,
        ),
    ]

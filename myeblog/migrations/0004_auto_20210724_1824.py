# Generated by Django 3.2.3 on 2021-07-24 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myeblog', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='insta_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

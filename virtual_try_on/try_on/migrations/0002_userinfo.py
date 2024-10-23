# Generated by Django 5.1 on 2024-10-19 14:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try_on', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_photos/')),
                ('body_type', models.CharField(choices=[('Apple', 'Apple'), ('Pear', 'Pear'), ('Hourglass', 'Hourglass'), ('Rectangle', 'Rectangle'), ('Curvy', 'Curvy'), ('Plus Size', 'Plus Size')], max_length=20)),
                ('skin_tone', models.CharField(choices=[('Fair', 'Fair'), ('Medium', 'Medium'), ('Olive', 'Olive'), ('Dark', 'Dark')], max_length=20)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(max_length=100)),
                ('age_group', models.CharField(choices=[('Teens', 'Teens (13-19)'), ('20s', '20s'), ('30s', '30s'), ('40s', '40s and above')], max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100)),
                ('typesOfClothes', models.CharField(choices=[('Casual', 'Casual'), ('Workwear', 'Workwear'), ('Social Ocassions', 'Social Ocassions'), ('Maternity', 'Maternity')], max_length=100)),
                ('sleeves', models.CharField(choices=[('Too short', 'Too short'), ('Just right', 'Just right'), ('Too Long', 'Too Long')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

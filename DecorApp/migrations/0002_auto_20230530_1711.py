# Generated by Django 3.2.10 on 2023-05-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DecorApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('password', models.IntegerField(blank=True, null=True)),
                ('confirmpassword', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cartdb',
            name='user',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
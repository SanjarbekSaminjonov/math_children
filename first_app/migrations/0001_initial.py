# Generated by Django 3.2.8 on 2021-10-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_answer', models.IntegerField(blank=True, null=True)),
                ('question_image', models.ImageField(upload_to='')),
            ],
        ),
    ]

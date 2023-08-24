# Generated by Django 4.2.4 on 2023-08-24 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreui', '0010_alter_skill_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistic', models.IntegerField()),
                ('claim', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=225)),
                ('bio', models.TextField(max_length=1000)),
            ],
        ),
    ]

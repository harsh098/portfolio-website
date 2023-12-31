# Generated by Django 4.2.4 on 2023-08-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreui', '0007_alter_contactinfo_facebook_alter_contactinfo_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='facebook',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='linkedin',
            field=models.URLField(default='https://www.linkedin.com/in/harsh-mishra-b94096144/'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='youtube',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]

# Generated by Django 2.0.4 on 2018-08-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnovationHubWebsite', '0010_job_special_marker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='file_path',
            new_name='file_path_stl',
        ),
        migrations.AddField(
            model_name='job',
            name='file_path_obj',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

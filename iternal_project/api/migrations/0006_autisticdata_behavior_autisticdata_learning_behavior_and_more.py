# Generated by Django 4.0.4 on 2022-06-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_autisticdata_clinical_history_significance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='autisticdata',
            name='behavior',
            field=models.TextField(default='NA'),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='learning_behavior',
            field=models.TextField(default='NA'),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='personal_developement',
            field=models.TextField(default='NA'),
        ),
    ]

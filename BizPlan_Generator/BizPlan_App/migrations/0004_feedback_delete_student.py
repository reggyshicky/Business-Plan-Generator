# Generated by Django 4.2.7 on 2023-11-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BizPlan_App', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

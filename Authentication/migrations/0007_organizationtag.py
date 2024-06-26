# Generated by Django 4.2.5 on 2024-05-13 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0006_alter_teacher_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationTag',
            fields=[
                ('tagId', models.AutoField(primary_key=True, serialize=False)),
                ('organizationName', models.CharField()),
                ('tagName', models.CharField(default='BoltAbacus', unique=True)),
                ('isIndividualTeacher', models.BooleanField(default=False)),
                ('numberOfTeachers', models.IntegerField(default=0)),
                ('numberOfStudents', models.IntegerField(default=0)),
                ('expirationDate', models.DateField(default=datetime.datetime.today)),
                ('totalNumberOfStudents', models.IntegerField(default=0)),
                ('maxLevel', models.IntegerField(default=1)),
                ('maxClass', models.IntegerField(default=1)),
            ],
        ),
    ]

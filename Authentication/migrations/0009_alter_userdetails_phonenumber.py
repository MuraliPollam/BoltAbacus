# Generated by Django 4.2.5 on 2023-09-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0008_alter_batch_classid_teacher_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='phoneNumber',
            field=models.CharField(max_length=10),
        ),
    ]

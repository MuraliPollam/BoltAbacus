# Generated by Django 4.2.5 on 2023-09-30 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0009_alter_userdetails_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='classId',
            new_name='class_Id',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='quizId',
            new_name='quiz_Id',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='userId',
            new_name='user_Id',
        ),
        migrations.RenameField(
            model_name='quizquestions',
            old_name='quizId',
            new_name='quiz_Id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='batchId',
            new_name='batch_Id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='userId',
            new_name='user_Id',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='batchId',
            new_name='batch_Id',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='userId',
            new_name='user_Id',
        ),
    ]
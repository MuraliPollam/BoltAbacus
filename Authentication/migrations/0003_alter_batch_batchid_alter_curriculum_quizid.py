# Generated by Django 4.2.5 on 2023-10-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_alter_quizquestions_questionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batchId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='quizId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-21 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batchId', models.IntegerField(primary_key=True, serialize=False)),
                ('timeDay', models.CharField()),
                ('timeSchedule', models.CharField()),
                ('numberOfStudents', models.IntegerField()),
                ('active', models.BooleanField()),
                ('batchName', models.CharField()),
                ('latestLevelId', models.IntegerField()),
                ('latestClassId', models.IntegerField()),
                ('latestLink', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('quizId', models.IntegerField(primary_key=True, serialize=False)),
                ('levelId', models.IntegerField()),
                ('classId', models.IntegerField()),
                ('topicId', models.IntegerField()),
                ('quizType', models.CharField(max_length=50)),
                ('quizName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TopicDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levelId', models.IntegerField()),
                ('classId', models.IntegerField()),
                ('topicId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField()),
                ('encryptedPassword', models.CharField()),
                ('created_date', models.DateField()),
                ('blocked', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchId', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Authentication.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Authentication.batch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Authentication.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestions',
            fields=[
                ('questionId', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField()),
                ('correctAnswer', models.CharField()),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('time', models.IntegerField()),
                ('quizPass', models.BooleanField(default=False)),
                ('percentage', models.FloatField(default=0)),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.curriculum')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.userdetails')),
            ],
        ),
    ]

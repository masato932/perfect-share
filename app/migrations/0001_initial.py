# Generated by Django 3.1.13 on 2021-07-18 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='タスク名')),
                ('duration', models.IntegerField(verbose_name='所要時間')),
                ('sharing_rate', models.IntegerField(verbose_name='分担率')),
                ('wage', models.IntegerField(verbose_name='賃金換算')),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2021-03-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=32, verbose_name='密码')),
                ('phone_num', models.CharField(max_length=32, verbose_name='手机号码')),
                ('email', models.EmailField(max_length=32, verbose_name='邮箱')),
            ],
        ),
    ]

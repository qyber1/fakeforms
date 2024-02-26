# Generated by Django 5.0.2 on 2024-02-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_verify',
            field=models.BooleanField(default=False, verbose_name='Подтвержденнный Email'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='answer',
            field=models.CharField(max_length=256, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='question',
            field=models.CharField(max_length=256, verbose_name='Вопрос'),
        ),
    ]
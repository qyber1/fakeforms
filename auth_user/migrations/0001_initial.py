# Generated by Django 5.0.2 on 2024-02-24 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('email_verify', models.BooleanField(default=False)),
                ('bis_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='type', to='quiz.businesstype', verbose_name='Ниша')),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cat', to='quiz.businesscategory', verbose_name='Категория бизнеса')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=256, null=True, verbose_name='Вопрос')),
                ('answer', models.CharField(blank=True, max_length=256, null=True, verbose_name='Ответ')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='auth_user.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Результат пользователя',
                'verbose_name_plural': 'Результаты пользователей',
            },
        ),
    ]
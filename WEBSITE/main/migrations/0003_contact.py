# Generated by Django 4.1.2 on 2022-12-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about_alter_task_options_alter_task_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Вид телефонной связи(мобильный,рабочий)')),
                ('about', models.IntegerField(verbose_name='Номер телефона(37529...)')),
                ('title_1', models.CharField(max_length=30, verbose_name='Название почты')),
                ('about_2', models.EmailField(max_length=254, verbose_name='Адресс электронной почты')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]

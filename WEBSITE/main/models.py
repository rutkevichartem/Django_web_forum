from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=30)
    task = models.TextField('Описание')
    data = models.DateTimeField()
    mail = models.EmailField('Адресс электронной почты')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class About(models.Model):
    title = models.CharField('Название', max_length=50)
    about = models.TextField('Описание')
    title_1 = models.CharField('Название', max_length=50)
    about_2 = models.TextField('Описание')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Contact(models.Model):
    title = models.CharField('Вид телефонной связи(мобильный,рабочий)', max_length=30)
    about = models.IntegerField('Номер телефона(37529...)')
    title_1 = models.CharField('Название почты', max_length=30)
    about_2 = models.EmailField('Адресс электронной почты')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
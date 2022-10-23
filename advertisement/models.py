from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Заголовок', db_index=True)
    descriptions = models.CharField(max_length=1000, default='', verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    count_views = models.IntegerField(verbose_name='Просмотры', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, verbose_name='Статус',
                               on_delete=models.CASCADE, related_name='advertisements')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, verbose_name='Тип объявления',
                             on_delete=models.CASCADE, related_name='advertisements')
    author = models.ForeignKey('Author', default=None, null=True, verbose_name='Автор',
                               on_delete=models.CASCADE, related_name='advertisements')
    phone = models.ForeignKey('Phone', default=None, null=True, verbose_name='Телефон',
                              on_delete=models.CASCADE, related_name='advertisements')
    email = models.ForeignKey('Email', default=None, null=True, verbose_name='Эл.почта',
                              on_delete=models.CASCADE, related_name='advertisements')

    class Meta:
        db_table = 'advertisement'
        ordering = ['title']

    def __str__(self):
        return self.title


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок', db_index=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.number


class Email(models.Model):
    mail = models.CharField(max_length=50)

    def __str__(self):
        return self.mail
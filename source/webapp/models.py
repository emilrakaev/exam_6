from django.db import models

DEFAULT_STATUS = 'other'
STATUS_CHOICES = [
    (DEFAULT_STATUS, 'Активно'),
    ('blocked', 'Заблокировано'),
]


class Guest(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=254, verbose_name='Почта')
    text = models.TextField(max_length=2000, verbose_name='Текст записи')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.TextField(max_length=50, choices = STATUS_CHOICES,
                              default=DEFAULT_STATUS, verbose_name='Статус')

    def __str__(self):
        return f'{self.name} - {self.status}'

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'

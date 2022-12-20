from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

User = get_user_model()


class Address(models.Model):
    address = models.CharField(
        verbose_name='адресс местонахождения',
        max_length=250,
    )

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адресы'
        ordering = ['id']

    def __str__(self) -> str:
        return self.address


class Items(models.Model):
    """Модель список итемов для инвентаризации."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='за кем числиться'
    )
    inventory_number = models.IntegerField(
        verbose_name='инвентарный номер',
        unique=True,
        validators=(
            validators.MinValueValidator(
                1, message='Минимальное значение 1'),
        ),
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='адресс местонахождения',
    )
    location = models.CharField(
        verbose_name='местонахождение по адресу',
        max_length=250,
    )
    room = models.CharField(
        verbose_name='помещение',
        max_length=150,
    )
    clear_name = models.CharField(
        verbose_name='понятное название',
        max_length=100,
    )
    brand_or_model = models.CharField(
        verbose_name='бренд / модель',
        max_length=100,
    )
    serial_number = models.CharField(
        verbose_name='серийный номер',
        max_length=100,
    )
    owner = models.CharField(
        verbose_name='за кем числиться',
        max_length=150,
    )
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='items/images/'
    )
    remark = models.CharField(
        verbose_name='примечание',
        max_length=250,
    )

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
        ordering = ['id']

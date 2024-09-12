from django.db import models

class Company(models.Model):
    """
    Модель для представления компании.

    Атрибуты:
        name (CharField): Название компании.
        company_type (CharField): Тип компании. Возможные значения:
            - 'factory': Завод
            - 'retail_network': Розничная сеть
            - 'individual_business': Индивидуальное предприниматель
        email (EmailField): Электронная почта компании.
        country (CharField): Страна, в которой расположена компания.
        city (CharField): Город, в котором расположена компания.
        street (CharField): Улица, на которой расположена компания.
        house_number (CharField): Номер дома компании.
        supplier (ForeignKey): Ссылка на другого поставщика (саму компанию), если есть.
        debt (DecimalField): Задолженность перед поставщиком, если имеется.
        created_at (DateTimeField): Дата и время создания записи о компании.
    """
    name = models.CharField(max_length=200, verbose_name='Название компании')
    company_type_choices = [
        ('factory', 'Завод'),
        ('retail_network', 'Розничная сеть'),
        ('individual_business', 'Индивидуальное предприниматель'),
    ]
    company_type = models.CharField(
        max_length=20,
        choices=company_type_choices,
        verbose_name='Тип компании'
    )
    email = models.EmailField(max_length=150, verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house_number = models.CharField(max_length=10, verbose_name='номер дома')
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='clients',
        verbose_name='поставщик')
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Задолженность перед поставщиком',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        """
        Возвращает строковое представление объекта компании.

        Returns:
            str: Название компании.
        """
        return self.name

    @property
    def company_level(self):
        """
        Определяет уровень компании на основе её типа и уровня поставщика.

        Returns:
            int: Уровень компании.
                - 0: Завод
                - 1: Розничная сеть, если не является поставщиком
                - Уровень поставщика + 1: Иное
        """
        if self.company_type == 'factory':
            return 0
        if not self.supplier:
            return 2
        return self.supplier.company_level + 1

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Product(models.Model):
    """
    Модель для представления продукта.

    Атрибуты:
        name (CharField): Название продукта.
        model (CharField): Модель продукта.
        release_date (DateField): Дата выпуска продукта.
        company (ForeignKey): Компания-владелец продукта.
    """
    name = models.CharField(max_length=200, verbose_name='Название товара')
    model = models.CharField(max_length=200, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выпуска')
    company = models.ForeignKey(Company,
                                related_name='products',
                                on_delete=models.CASCADE,
                                verbose_name='Компания-владелец')

    def __str__(self):
        """
        Возвращает строковое представление объекта продукта.

        Returns:
            str: Название и модель продукта в формате "Название (Модель)".
        """
        return f'{self.name} ({self.model})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

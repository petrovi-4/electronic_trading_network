from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from company.models import Company, Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Админка для управления моделями Company в Django Admin.
    Показывает список компаний с возможностью фильтрации, поиска и выполнения действий.
    """
    list_display = (
        'pk',
        'name',
        'email',
        'country',
        'city',
        'view_supplier_link',
        'debt',
        'created_at'
    )
    list_filter = ('city',)
    search_fields = ('name',)
    actions = ['clear_debt']

    def view_supplier_link(self, obj):
        """
        Отображает ссылку на поставщика компании в админке.
        Если у компании есть поставщик, возвращает HTML-ссылку на страницу редактирования
        этого поставщика. В противном случае возвращает строку '-'.

        Args:
            obj (Company): Экземпляр компании.
        Returns:
            str: HTML-код ссылки или строка '-'.
        """
        if obj.supplier:
            url = reverse("admin:company_company_change", args=[obj.supplier.pk])
            return format_html('<a href="{}">{}</a>', url, obj.supplier)
        return "-"

    view_supplier_link.short_description = "Поставщик"

    def clear_debt(self, request, queryset):
        """
        Обнуляет задолженность для выбранных компаний.
        Этот метод вызывается как действие в админке для выбранных записей.

        Args:
            request (HttpRequest): Объект запроса.
            queryset (QuerySet): Выбранные записи в админке.
        """
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админка для управления моделями Product в Django Admin.
    Показывает список продуктов с возможностью фильтрации и поиска.
    """
    list_display = ('pk', 'name', 'model', 'release_date', 'company')
    list_filter = ('company',)
    search_fields = ('name', 'model')

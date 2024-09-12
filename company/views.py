from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from company.filters import CompanyFilter
from company.models import Company
from company.permissions import IsActiveEmployee
from company.serializers import CompanyDetailSerializer, CompanySerializer


class CompanyCreateAPIView(generics.CreateAPIView):
    """Эндпоинт для создания компании."""
    serializer_class = CompanyDetailSerializer
    permission_classes = [IsActiveEmployee]


class CompanyListAPIView(generics.ListAPIView):
    """Эндпоинт для получения списка компаний."""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompanyFilter
    permission_classes = [IsActiveEmployee]


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт для получения детальной информации о компани."""
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    permission_classes = [IsActiveEmployee]


class CompanyUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт для изменения информации о компании."""
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    permission_classes = [IsActiveEmployee]

    def performn_update(self, serializer):
        """
        Сохраняет обновлённый объект компании.
        Переопределяет метод, чтобы сохранить задолженность, как она была до обновления.
        """
        serializer.save(debt=self.get_object().debt)


class CompanyDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт для удаления компании."""
    queryset = Company.objects.all()
    permission_classes = [IsActiveEmployee]

from django.urls import path

from company.views import CompanyCreateAPIView, CompanyListAPIView, \
    CompanyRetrieveAPIView, CompanyUpdateAPIView, \
    CompanyDestroyAPIView

urlpatterns = [
    path('create/', CompanyCreateAPIView.as_view(), name='company-create'),
    path('', CompanyListAPIView.as_view(), name='company-list'),
    path('<int:pk>/', CompanyRetrieveAPIView.as_view(), name='company-retrieve'),
    path('<int:pk>/update/', CompanyUpdateAPIView.as_view(), name='company-update'),
    path('<int:pk>/delete/', CompanyDestroyAPIView.as_view(), name='company-delete'),
]

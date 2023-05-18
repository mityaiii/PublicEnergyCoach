from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProductAPIView().as_view(), name="products"),
    path('category/<str:category>/', views.ProductsByCategoryAPIView.as_view(), name='products'),
    path('<key>/', views.ProductAPIView.as_view(), name='products'),
]

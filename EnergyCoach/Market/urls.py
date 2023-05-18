from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllMarketProductAPIView().as_view(), name="market_products"),
    path('category/<str:category>/', views.MarketProductsByCategoryAPIView.as_view(), name='market_products'),
    path('<key>/', views.MarketProductAPIView.as_view(), name='market_products'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllBlogAPIView().as_view(), name="blogs"),
    path('category/<str:category>/', views.BlogsByCategoryAPIView.as_view(), name='blogs'),
    path('<key>/', views.BlogAPIView.as_view(), name='blogs'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('add_contact/', views.ContactFormAPIView.as_view()),
    path('meta/<key>', views.MetaAPIView.as_view()),
]

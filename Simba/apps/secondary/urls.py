from django.urls import path
from .views import about, faqs

urlpatterns = [
    path('about/', about, name="about"),
    path('faqs/', faqs, name="faqs"),
]

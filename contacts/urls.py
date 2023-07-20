from django.urls import path
from .views import ContactList, ContactDetail, api_root

urlpatterns = [
    path("contacts/", ContactList.as_view(), name="contact-list"),
    path("contacts/<int:pk>", ContactDetail.as_view(), name="contact-detail"),
    path("", api_root),
]

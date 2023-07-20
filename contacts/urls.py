from django.urls import path
from .views import ContactList

urlpatterns = [
    path("contacts/", ContactList.as_view(), name="contact-list-create"),
]

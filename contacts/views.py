from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "contacts": reverse("contact-list", request=request, format=format),
        }
    )

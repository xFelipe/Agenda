from rest_framework.viewsets import ModelViewSet
from agenda.core.api.serializers import ContactSeriealizer
from agenda.core.models import Contact


class ContactsViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSeriealizer
    http_method_names = ['get', 'post', 'delete', 'put']

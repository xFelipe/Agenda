from rest_framework import serializers
from agenda.core.models import Contact


class ContactSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'nome', 'canal', 'valor', 'obs')

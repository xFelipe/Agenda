from rest_framework import serializers
from agenda.core.models import Contact
from rest_framework.renderers import JSONRenderer


class ContactSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'nome', 'canal', 'valor', 'obs')

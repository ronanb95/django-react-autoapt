from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('id', 'area', 'title', 'published', 'rooms', 'size', 'description', 'landlord')
        write_only_fields = ['landlord'] # TODO: This does not work, need to fix
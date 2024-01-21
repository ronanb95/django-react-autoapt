from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer


class AllListings(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class SingleListing(generics.RetrieveDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

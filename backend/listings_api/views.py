from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer
from .permissions import ListingEditPermission
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

#TODO: Restrict creation to Landlords, restict creation to one every couple of minutes
class AllListings(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class SingleListing(generics.RetrieveAPIView, generics.UpdateAPIView, ListingEditPermission):
    permission_classes = [ListingEditPermission]
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

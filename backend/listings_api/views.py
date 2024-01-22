from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer
from .permissions import ListingEditPermission
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# class Listings(viewsets.ModelViewSet):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     serializer_class = ListingSerializer
#     #queryset = Listing.objects.all()

#     #Define a custom query set
#     def get_queryset(self):
#         return Listing.objects.all()

class Listings(viewsets.ViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Listing.listingobjects.all()

    def list(self, request):
        serializer_class = ListingSerializer(self.queryset, many=True)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk=None):
        listing = get_object_or_404(self.queryset, pk=pk)
        serializer_class = ListingSerializer(listing)
        return Response(serializer_class.data)

    # def create(self, request):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
    
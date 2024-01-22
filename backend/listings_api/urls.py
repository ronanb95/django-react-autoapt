from django.urls import path
from .views import AllListings, SingleListing

app_name = 'listings_api'

urlpatterns = [
    path('<int:pk>/', SingleListing.as_view(), name='detailcreate'),
    path('', AllListings.as_view(), name='listcreate'),
]
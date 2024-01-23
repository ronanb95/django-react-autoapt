from rest_framework.routers import DefaultRouter
from .views import Listings

app_name = 'listings_api'

router = DefaultRouter()
router.register('', Listings, basename='listing')
urlpatterns = router.urls


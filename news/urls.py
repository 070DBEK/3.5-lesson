from rest_framework.routers import DefaultRouter
from .views import NewViewSet


router = DefaultRouter()
router.register(r'news', NewViewSet, basename='new')

urlpatterns = router.urls

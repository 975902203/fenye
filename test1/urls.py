from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
import views

router = DefaultRouter()
router.register(r'select', views.SelectViewSet, base_name='message')

urlpatterns = router.urls
print(urlpatterns)
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('charger_type', ChargerTypeViewSet)
router.register('client', ClientViewSet)
router.register('charger_stations', ChargeStationsViewSet)
router.register('charger_points', ChargePointsViewSets)
#router.register(r'^history', HistoryViewSets)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^uploaddata', uploaddata),
    url(r'^near_point', near_point),
]

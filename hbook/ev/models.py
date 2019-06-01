from django.db import models
from hbook.users.models import User2
from rest_framework.serializers import HyperlinkedModelSerializer

class ChargerType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    others = models.TextField(default='{}')

class ChargerTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ChargerType
        fields = ('name', 'pk', 'others')

class Client(models.Model):
    user = models.ForeignKey(User2, on_delete=models.CASCADE)
    vehicle = models.CharField(max_length=50)    
    charger_type = models.ForeignKey(ChargerType, on_delete=models.CASCADE)

class ClientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('user', 'pk', 'user', 'vehicle', 'charger_type')
    
class ChargeStation(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    dealer = models.CharField(max_length=250, default="")
    address = models.CharField(max_length=300, default="")


class ChargePoints(models.Model):
    charge_station = models.ForeignKey(ChargeStation, on_delete=models.CASCADE, related_name="points")
    charger_type = models.ForeignKey(ChargerType, on_delete=models.CASCADE, related_name="points")
    slots = models.PositiveIntegerField(default=1)
    slots_occupied = models.PositiveIntegerField(default=0)

class ChargePointsSerializer(HyperlinkedModelSerializer):
    charger_type = ChargerTypeSerializer()
    class Meta:
        model = ChargePoints
        fields = ('pk', 'charger_type', 'slots', 'slots_occupied')


class ChargeStationSerializer(HyperlinkedModelSerializer):
    points = ChargePointsSerializer(many=True)
    class Meta:
        model = ChargeStation
        fields = ('pk', 'lat', 'long', 'points')

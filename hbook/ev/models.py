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
    data = models.TextField(default="""{
    "wall": 0,
    "j-1772": 0,
    "CHAdeMO": 0,
    "Tesla(roadster)": 0,
    "NEMA 14-50": 0,
    "Tesla": 0,
    "Type-2": 0,
    "Type-3": 0,
    "wall(BS1361)": 0,
    "Wall(euro)": 0,
    "Commando": 0,
    "wall(AU/NZ)": 0,
    "Caravan Mains": 0,
    "CCS/SAE": 0,
    "THREEPhase": 0,

    "wall-a": 0,
    "j-1772-a": 0,
    "CHAdeMO-a": 0,
    "Tesla(roadster)-a": 0,
    "NEMA 14-50-a": 0,
    "Tesla-a": 0,
    "Type-2-a": 0,
    "Type-3-a": 0,
    "wall(BS1361)-a": 0,
    "Wall(euro)-a": 0,
    "Commando-a": 0,
    "wall(AU/NZ)-a": 0,
    "Caravan Mains-a": 0,
    "CCS/SAE-a": 0,
    "THREEPhase-a": 0
    }""")


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
    # points = ChargePointsSerializer(many=True)
    class Meta:
        model = ChargeStation
        fields = ('pk', 'lat', 'long', "address", "dealer", "data")

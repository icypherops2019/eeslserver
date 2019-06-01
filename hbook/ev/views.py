from rest_framework.viewsets import ModelViewSet
from .models import *
from django.http import HttpResponse

class ChargerTypeViewSet(ModelViewSet):
    queryset = ChargerType.objects.all()
    serializer_class = ChargerTypeSerializer

class ClientViewSet(ModelViewSet):
    queryset =  Client.objects.all()
    serializer_class = ClientSerializer

class ChargeStationsViewSet(ModelViewSet):
    queryset = ChargeStation.objects.all()
    serializer_class = ChargeStationSerializer

class ChargePointsViewSets(ModelViewSet):
    queryset = ChargePoints.objects.all()
    serializer_class = ChargePointsSerializer

class HistoryViewSets(ModelViewSet):
    pass

def uploaddata(request):
    y,z = int(request.GET.get("y", "0")), int(request.GET.get("z", "10"))
    file = open("hbook/ev/csvjson.json", "r")
    import json
    data = json.loads(file.read())
    file.close()
    cols = [x for x in data[0].keys() if x not in ['latitude', 'longitude', 'Dealer', 'Address']]
    # pushing this values as type 
    d = {}
    for x in cols:
        # first search for same name
        t = ChargerType.objects.all().filter(name = x)
        if len(t) == 0:
            t = ChargerType()
            t.name = x
            t.save()
        else:
            t = t[0]
        d[x] = t
     
    for i in range(len(data)):
        if i<y: continue
        if i>z: break
        x = data[i]
        station = ChargeStation()
        station.name = "-"
        station.address = x['Address']
        station.dealer = x['Dealer']
        station.lat = x['latitude']
        station.long = x['longitude']
        station.save()
        for xx in cols:
            if x[xx] != 0:
                point = ChargePoints()
                point.charge_station = station
                point.charger_type = d[xx]
                point.slots = x[xx]
                point.save()
    return HttpResponse("")
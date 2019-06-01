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
    y,z = int(request.GET.get("y", "0")), int(request.GET.get("z", "1000"))
    file = open("hbook/ev/csvjson.json", "r")
    import json
    data = json.loads(file.read())
    file.close()
    cols = [x for x in data[0].keys() if x not in ['latitude', 'longitude', 'Dealer', 'Address']]
     
    for i in range(len(data)):
        if i<y: continue
        if i>z: break
        x = data[i]
        station = ChargeStation()
        station.address = x['Address']
        station.dealer = x['Dealer']
        station.lat = x['latitude']
        station.long = x['longitude']
        d = {}
        for xx in cols:
            d[xx] = data[i][xx]
            d[xx+"-a"] = 0
        station.data = json.dumps(d)
        station.save()
    
    return HttpResponse("Data Uploaded successfully")
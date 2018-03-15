import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD2Project.settings')

import django
django.setup()
from pubway.models import Station, Place
from datetime import time

def populate():

    stations = {
        "Hillhead": {"stringName":"Hillhead", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.875236, "longitude":-4.293352},
        "Kelvinbridge": {"stringName":"Kelvinbridge", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.874307, "longitude":-4.279574},
        "StGeorgesCross": {"stringName":"St. George's Cross", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.871200, "longitude":-4.269180},
        "Cowcaddens": {"stringName":"Cowcaddens", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.869111, "longitude":-4.259755},
        "BuchananStreet": {"stringName":"Buchanan Street", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.862401, "longitude":-4.253383},
        "StEnoch": {"stringName":"St. Enoch", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.857554, "longitude":-4.255175},
        "BridgeStreet": {"stringName":"Bridge Street", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.852080, "longitude":-4.258563},
        "WestStreet": {"stringName":"West Street", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.849534, "longitude":-4.265919},
        "ShieldsRoad": {"stringName":"Shields Road", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.850000, "longitude":-4.275344},
        "KinningPark": {"stringName":"Kinning Park", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.850505, "longitude":-4.287747},
        "Cessnock": {"stringName":"Cessnock", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.852052, "longitude":-4.294296},
        "Ibrox": {"stringName":"Ibrox", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.854610, "longitude":-4.304480},
        "Govan": {"stringName":"Govan", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.662189, "longitude":-4.310560},
        "Partick": {"stringName":"Partick", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.869841, "longitude":-4.308683},
        "Kelvinhall": {"stringName":"Kelvinhall", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.870939, "longitude":-4.299956}
    }
    places = {
        "QMU": {"pc":"G12 8QN", "adr":"22 University Gardens, Glasgow", "web":"qmunion.org.uk", "closeSt":"Hillhead", "type":"Pub",},
        "GUU": {"pc":"G12 8LX", "adr":"32 University Avenue, Glasgow", "web":"guu.co.uk", "closeSt":"Kelvin Bridge", "type":"Pub",},
        "Bank Street": {"pc":"G12 8LZ", "adr":"52 Bank St, Glasgow G12 8LZ", "web":"bankst.co.uk", "closeSt":"Kelvin Bridge", "type":"Pub",},
        "The Sparkle Horse": {"pc":"G11 5QR", "adr":"Dowanhill St, Glasgow", "web":"thesparklehorse.com", "closeSt":"", "type":"Restaurant",},
        "Pizza Crolla": {"pc":"G1 2LL", "adr":"156 Buchanan St, Glasgow", "web":None, "closeSt":"Buchanan Street", "type":"Restaurant",},
        #"": {"pc":"G", "adr":"", "web":"", "closeSt":"", "type":"",},
    }

    for station,station_data in stations.items():
        s = add_station(station,station_data["stringName"],station_data["firstTrainMonSat"],station_data["lastTrainMonSat"],station_data["firstTrainSun"],station_data["lastTrainSun"],station_data["latitude"],station_data["longitude"])

    for s in Station.objects.all():
            print("- {0}".format(str(s)))

def add_station(name,stringName,firstTrainMonSat,lastTrainMonSat,firstTrainSun,lastTrainSun,latitude,longitude):
    s = Station.objects.get_or_create(name=name)[0]
    s.stringName=stringName
    s.firstTrainMonSat=firstTrainMonSat
    s.lastTrainMonSat=lastTrainMonSat
    s.firstTrainSun=firstTrainSun
    s.lastTrainSun=lastTrainSun
    s.latitude=latitude
    s.longitude=longitude
    s.save()
    return s

def add_place(name, data):
    p = Place.objects.get_or_create(name=name)
    


if __name__ == '__main__':
    print("Running pubway population script...")
    populate()
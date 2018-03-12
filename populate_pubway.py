import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD2Project.settings')

import django
django.setup()
from pubway.models import Station
from datetime import time

def populate():

    stations = {
        "Hillhead": {"stringName":"Hillhead", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Kelvinbridge": {"stringName":"Kelvinbridge", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "StGeorgesCross": {"stringName":"St. George's Cross", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Cowcaddens": {"stringName":"Cowcaddens", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "BuchananStreet": {"stringName":"Buchanan Street", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "StEnoch": {"stringName":"St. Enoch", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "BridgeStreet": {"stringName":"Bridge Street", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "WestStreet": {"stringName":"West Street", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "ShieldsRoad": {"stringName":"Shields Road", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "KinningPark": {"stringName":"Kinning Park", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Cessnock": {"stringName":"Cessnock", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Ibrox": {"stringName":"Ibrox", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Govan": {"stringName":"Govan", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Partick": {"stringName":"Partick", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Kelvinhall": {"stringName":"Kelvinhall", "firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)}
    }

    for station,station_data in stations.items():
        s = add_station(station,station_data["stringName"],station_data["firstTrainMonSat"],station_data["lastTrainMonSat"],station_data["firstTrainSun"],station_data["lastTrainSun"])

def add_station(name,stringName,firstTrainMonSat,lastTrainMonSat,firstTrainSun,lastTrainSun):
    s = Station.objects.get_or_create(name=name)[0]
    s.stringName=stringName
    s.firstTrainMonSat=firstTrainMonSat
    s.lastTrainMonSat=lastTrainMonSat
    s.firstTrainSun=firstTrainSun
    s.lastTrainSun=lastTrainSun
    s.save()
    return s

if __name__ == '__main__':
    print("Running pubway population script...")
    populate()
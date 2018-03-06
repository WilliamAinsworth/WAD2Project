import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD2Project.settings')

import django
django.setup()
from pubway.models import Station
from datetime import time

def populate():

    stations = {
        "Hillhead": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Kelvinbridge": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "StGeorgesCross": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Cowcaddens": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "BuchananStreet": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "StEnoch": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "BridgeStreet": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "WestStreet": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "ShieldsRoad": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "KinningPark": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Cessnock": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Ibrox": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Govan": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Partick": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)},
        "Kelvinhall": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30)}
    }

    for station,station_data in stations.items():
        s = add_station(station,station_data["firstTrainMonSat"],station_data["lastTrainMonSat"],station_data["firstTrainSun"],station_data["lastTrainSun"])

def add_station(name,firstTrainMonSat,lastTrainMonSat,firstTrainSun,lastTrainSun):
    s = Station.objects.get_or_create(name=name)[0]
    s.firstTrainMonSat=firstTrainMonSat
    s.lastTrainMonSat=lastTrainMonSat
    s.firstTrainSun=firstTrainSun
    s.lastTrainSun=lastTrainSun
    s.save()
    return s

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
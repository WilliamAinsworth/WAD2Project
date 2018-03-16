import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD2Project.settings')

import django
django.setup()
from pubway.models import Station, Place
from datetime import time

def populate():

    stations = {
        "Hillhead": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.875236, "longitude":-4.293352},
        "Kelvinbridge": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.874307, "longitude":-4.279574},
        "St. George's Cross": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.871200, "longitude":-4.269180},
        "Cowcaddens": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.869111, "longitude":-4.259755},
        "Buchanan Street": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.862401, "longitude":-4.253383},
        "St. Enoch": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.857554, "longitude":-4.255175},
        "Bridge Street": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.852080, "longitude":-4.258563},
        "West Street": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.849534, "longitude":-4.265919},
        "Shields Road": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.850000, "longitude":-4.275344},
        "Kinning Park": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.850505, "longitude":-4.287747},
        "Cessnock": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.852052, "longitude":-4.294296},
        "Ibrox": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.854610, "longitude":-4.304480},
        "Govan": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.662189, "longitude":-4.310560},
        "Partick": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.869841, "longitude":-4.308683},
        "Kelvinhall": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 30),"latitude":55.870939, "longitude":-4.299956}
    }
    places = {
        "QMU": {"postcode":"G12 8QN", "address":"22 University Gardens, Glasgow", "website":"qmunion.org.uk", "closeStation":Station(name='Hillhead'), "type":1},
        "GUU": {"postcode":"G12 8LX", "address":"32 University Avenue, Glasgow", "website":"guu.co.uk", "closeStation":Station(name='Kelvinbridge'), "type":1},
        "Bank Street": {"postcode":"G12 8LZ", "address":"52 Bank St, Glasgow G12 8LZ", "website":"bankst.co.uk", "closeStation":Station(name='Kelvinbridge'), "type":1},
        "The Sparkle Horse": {"postcode":"G11 5QR", "address":"Dowanhill St, Glasgow", "website":"thesparklehorse.com", "closeStation": Station(name='Kelvinhall'), "type":2},
        "Pizza Crolla": {"postcode":"G1 2LL", "address":"156 Buchanan St, Glasgow", "website":"", "closeStation":Station(name='Buchanan Street'), "type":2},
    }

    for station,station_data in stations.items():
        s = add_station(station,station_data["firstTrainMonSat"],station_data["lastTrainMonSat"],station_data["firstTrainSun"],station_data["lastTrainSun"],station_data["latitude"],station_data["longitude"])

    print("Populating subway stations...")
    for s in Station.objects.all():
            print("- {0}".format(str(s)))

    for place,place_data in places.items():
        p = add_place(place,place_data["postcode"],place_data["address"],place_data["website"],place_data["closeStation"],place_data["type"])

    print("Populating places ...")
    for p in Place.objects.all():
            print("- {0} near {1}".format(str(p), str(p.closeStation)))

def add_station(name,firstTrainMonSat,lastTrainMonSat,firstTrainSun,lastTrainSun,latitude,longitude):
    s = Station.objects.get_or_create(name=name)[0]
    s.firstTrainMonSat=firstTrainMonSat
    s.lastTrainMonSat=lastTrainMonSat
    s.firstTrainSun=firstTrainSun
    s.lastTrainSun=lastTrainSun
    s.latitude=latitude
    s.longitude=longitude
    s.save()
    return s

def add_place(name,postcode,address,website,closeStation,type):
    p = Place.objects.get_or_create(name=name)[0]
    p.postcode = postcode
    p.address = address
    p.website = website
    p.closeStation = closeStation
    p.type = type
    p.save()
    return p

if __name__ == '__main__':
    print("Running pubway population script...")
    populate()


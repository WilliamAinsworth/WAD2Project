import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD2Project.settings')

import django
django.setup()
from pubway.models import Station, Place
from datetime import time

def populate():

    stations = {
        "Hillhead": {"firstTrainMonSat": time(6, 36), "lastTrainMonSat": time(23, 22), "firstTrainSun": time(10, 6), "lastTrainSun": time(17, 56),"latitude":55.875236, "longitude":-4.293352, "mapCoords":"220,30,360,80" },
        "Kelvinbridge": {"firstTrainMonSat": time(6, 38), "lastTrainMonSat": time(23, 24), "firstTrainSun": time(10, 8), "lastTrainSun": time(17, 58),"latitude":55.874307, "longitude":-4.279574, "mapCoords":"400,10,600,50"},
        "St. George's Cross": {"firstTrainMonSat": time(6, 40), "lastTrainMonSat": time(23, 26), "firstTrainSun": time(10, 10), "lastTrainSun": time(18, 0),"latitude":55.871200, "longitude":-4.269180, "mapCoords":"610,10,780,80"},
        "Cowcaddens": {"firstTrainMonSat": time(6, 42), "lastTrainMonSat": time(23, 28), "firstTrainSun": time(10, 12), "lastTrainSun": time(18, 1),"latitude":55.869111, "longitude":-4.259755, "mapCoords":"810,40,990,70"},
        "Buchanan Street": {"firstTrainMonSat": time(6, 44), "lastTrainMonSat": time(23, 29), "firstTrainSun": time(10, 14), "lastTrainSun": time(18, 2),"latitude":55.862401, "longitude":-4.253383, "mapCoords":"1000,100,1150,170"},
        "St. Enoch": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 00), "lastTrainSun": time(18, 4),"latitude":55.857554, "longitude":-4.255175, "mapCoords":"1070,260,1210,300"},
        "Bridge Street": {"firstTrainMonSat": time(6, 32), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 2), "lastTrainSun": time(18, 6),"latitude":55.852080, "longitude":-4.258563, "mapCoords":"1040,500,1130,580"},
        "West Street": {"firstTrainMonSat": time(6, 34), "lastTrainMonSat": time(23, 32), "firstTrainSun": time(10, 4), "lastTrainSun": time(18, 8),"latitude":55.849534, "longitude":-4.265919, "mapCoords":"900,620,1000,690"},
        "Shields Road": {"firstTrainMonSat": time(6, 36), "lastTrainMonSat": time(23, 34), "firstTrainSun": time(10, 6), "lastTrainSun": time(18, 10),"latitude":55.850000, "longitude":-4.275344, "mapCoords":"710,640,820,710"},
        "Kinning Park": {"firstTrainMonSat": time(6, 38), "lastTrainMonSat": time(23, 36), "firstTrainSun": time(10, 8), "lastTrainSun": time(18, 12),"latitude":55.850505, "longitude":-4.287747, "mapCoords":"530,640,660,710"},
        "Cessnock": {"firstTrainMonSat": time(6, 40), "lastTrainMonSat": time(23, 38), "firstTrainSun": time(10, 10), "lastTrainSun": time(18, 14),"latitude":55.852052, "longitude":-4.294296, "mapCoords":"350,640,500,690"},
        "Ibrox": {"firstTrainMonSat": time(6, 42), "lastTrainMonSat": time(23, 30), "firstTrainSun": time(10, 12), "lastTrainSun": time(17, 15),"latitude":55.854610, "longitude":-4.304480, "mapCoords":"200,620,280,660"},
        "Govan": {"firstTrainMonSat": time(6, 30), "lastTrainMonSat": time(23, 16), "firstTrainSun": time(10, 00), "lastTrainSun": time(17, 50),"latitude":55.662189, "longitude":-4.310560, "mapCoords":"60,510,160,550"},
        "Partick": {"firstTrainMonSat": time(6, 32), "lastTrainMonSat": time(23, 18), "firstTrainSun": time(10, 2), "lastTrainSun": time(17, 52),"latitude":55.869841, "longitude":-4.308683, "mapCoords":"0,260,110,300"},
        "Kelvinhall": {"firstTrainMonSat": time(6, 34), "lastTrainMonSat": time(23, 20), "firstTrainSun": time(10, 4), "lastTrainSun": time(17, 54),"latitude":55.870939, "longitude":-4.299956, "mapCoords":"50,110,210,150"}
    }
    places = {
        "QMU": {"postcode":"G12 8QN", "address":"22 University Gardens, Glasgow", "website":"qmunion.org.uk", "closeStation":Station(name='Hillhead'), "likes":72,"type":1},
        "GUU": {"postcode":"G12 8LX", "address":"32 University Avenue, Glasgow", "website":"guu.co.uk", "closeStation":Station(name='Kelvinbridge'), "likes": 12,"type":1},
        "Bank Street": {"postcode":"G12 8LZ", "address":"52 Bank St, Glasgow G12 8LZ", "website":"bankst.co.uk", "closeStation":Station(name='Kelvinbridge'), "likes":35,"type":1},
        "The Sparkle Horse": {"postcode":"G11 5QR", "address":"Dowanhill St, Glasgow", "website":"thesparklehorse.com", "closeStation": Station(name='Kelvinhall'), "likes":22,"type":2},
        "Pizza Crolla": {"postcode":"G1 2LL", "address":"156 Buchanan St, Glasgow", "website":"", "closeStation":Station(name='Buchanan Street'), "likes":5, "type":2},
        "Vodka Wodka": {"postcode":"G12 8SJ", "address":"31 Ashton Lane", "website":"http://vodkawodka.co.uk/a/","closeStation":Station(name='Hillhead'), "likes":255, "type":1},
        "Ashoka": {"postcode":"G12 8SJ", "address":"19 Ashton Lane", "website":"http://www.ashokaashtonlane.com/","closeStation":Station(name='Hillhead'), "likes":55, "type":2},
        "Cafe Andaluz": {"postcode": "G12 8AA", "address": "2 Cresswell Lane", "website": "","closeStation": Station(name='Hillhead'), "likes": 65, "type": 2},
        "Hillhead Bookclub": {"postcode": "G12 8BH", "address": "17 Cresswell Lane", "website": "http://hillheadbookclub.co.uk/","closeStation": Station(name='Hillhead'), "likes": 85, "type": 1},
    }

    for station,station_data in stations.items():
        s = add_station(station,station_data["firstTrainMonSat"],station_data["lastTrainMonSat"],station_data["firstTrainSun"],station_data["lastTrainSun"],station_data["latitude"],station_data["longitude"],station_data["mapCoords"])

    print("Populating subway stations...")
    for s in Station.objects.all():
            print("- {0}".format(str(s)))

    for place,place_data in places.items():
        p = add_place(place,place_data["postcode"],place_data["address"],place_data["website"],place_data["closeStation"],place_data["likes"],place_data["type"])

    print("Populating places ...")
    for p in Place.objects.all():
            print("- {0} near {1}".format(str(p), str(p.closeStation)))

def add_station(name,firstTrainMonSat,lastTrainMonSat,firstTrainSun,lastTrainSun,latitude,longitude,mapCoords):
    s = Station.objects.get_or_create(name=name)[0]
    s.firstTrainMonSat=firstTrainMonSat
    s.lastTrainMonSat=lastTrainMonSat
    s.firstTrainSun=firstTrainSun
    s.lastTrainSun=lastTrainSun
    s.latitude=latitude
    s.longitude=longitude
    s.mapCoords=mapCoords
    s.save()
    return s

def add_place(name,postcode,address,website,closeStation,likes,type):
    p = Place.objects.get_or_create(name=name)[0]
    p.postcode = postcode
    p.address = address
    p.website = website
    p.closeStation = closeStation
    p.likes=likes
    p.type = type
    p.save()
    return p

if __name__ == '__main__':
    print("Running pubway population script...")
    populate()


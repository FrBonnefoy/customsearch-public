import json
import urllib.request as urlreq
import urllib.parse
from pointage import adresses as adrsx


class searcher:
    def __init__(self,item):
        self.item=item
        search=urllib.parse.quote_plus(self.item)
        qpage="https://maps.googleapis.com/maps/api/geocode/json?address="+search+"&language=fr&key=INSERT API KEY HERE"
        query=urlreq.urlopen(qpage)
        self.data=query.read().decode('utf-8').replace('(','[').replace(')',']')

class searcher_detail:
    def __init__(self,item):
        self.item=item
        search=urllib.parse.quote_plus(self.item)
        qpage="https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="+search+"&inputtype=textquery&fields=place_id,name,formatted_address&key=INSERT API KEY HERE"
        query=urlreq.urlopen(qpage)
        self.data=query.read().decode('utf-8').replace('(','[').replace(')',']')

class parser_detail:
    def __init__(self,datax):
        self.data=json.loads(datax)
        self.place_id=None
        self.name=None
        self.adrs=None
        self.street_number=None
        self.road=None
        self.suburb=None
        self.city=None
        self.district=None
        self.postcode=None
        self.country=None

        try:
            place_id = self.data['candidates'][0]['place_id']
        except:
            place_id = ''
        try:
            name = self.data['candidates'][0]['name']
        except:
            name = ''
        try:
            adrs = self.data['candidates'][0]['formatted_address']
        except:
            adrs = ''

        self.place_id = place_id
        self.name = name
        self.adrs = adrs


        try:
            street_number = adrsx.parse_adrs(adrs).street_number
        except:
            street_number = ''

        try:
            road = adrsx.parse_adrs(adrs).road
        except:
            road = ''

        try:
            suburb = adrsx.parse_adrs(adrs).suburb
        except:
            suburb = ''

        try:
            city = adrsx.parse_adrs(adrs).city
        except:
            city = ''

        try:
            district = adrsx.parse_adrs(adrs).district
        except:
            district = ''

        try:
            postcode = adrsx.parse_adrs(adrs).postcode
        except:
            postcode = ''

        try:
            country = adrsx.parse_adrs(adrs).country
        except:
            country = ''

        self.street_number = street_number
        self.road = road
        self.suburb = suburb
        self.city = city
        self.district = district
        self.postcode = postcode
        self.country = country



class parser:
    def __init__(self,datax):
        self.data=json.loads(datax)
        self.street_number=None
        self.route=None
        self.neighborhood=None
        self.locality=None
        self.aa2=None
        self.aa1=None
        self.country=None
        self.code_postal=None
        self.lat=None
        self.lng=None
        self.bounds=None
        self.viewport=None
        self.faddress=None
        self.id=None
        self.ue=None




        try:
            for i in self.data['results'][0]['address_components']:
                if 'street_number' in i['types']:
                    self.street_number=i['long_name']
        except:
            self.street_number=""


        try:
            for i in self.data['results'][0]['address_components']:
                if 'route' in i['types']:
                    self.route=i['long_name']
        except:
            self.route=""


        try:
            for i in self.data['results'][0]['address_components']:
                if 'neighborhood' in i['types']:
                    self.neighborhood=i['long_name']
        except:
            self.neighborhood=""


        try:
            for i in self.data['results'][0]['address_components']:
                if 'locality' in i['types']:
                    self.locality=i['long_name']
        except:
            self.locality=""

        try:
            for i in self.data['results'][0]['address_components']:
                if 'administrative_area_level_2' in i['types']:
                    self.aa2=i['long_name']
        except:
            self.aa2=""

        try:
            for i in self.data['results'][0]['address_components']:
                if 'administrative_area_level_1' in i['types']:
                    self.aa1=i['long_name']
        except:
            self.aa1=""

        try:
            for i in self.data['results'][0]['address_components']:
                if 'country' in i['types']:
                    self.country=i['long_name'].upper()
        except:
            self.country=""

        try:
            for i in self.data['results'][0]['address_components']:
                if 'postal_code' in i['types']:
                    self.code_postal=i['long_name']
        except:
            self.code_postal=""

        try:
            self.lat=self.data['results'][0]['geometry']['location']['lat']
        except:
            self.lat=""

        try:
            self.lng=self.data['results'][0]['geometry']['location']['lng']
        except:
            self.lng=""

        try:
            self.bounds=self.data['results'][0]['geometry']['bounds']
        except:
            self.bounds=""

        try:
            self.viewport=self.data['results'][0]['geometry']['viewport']
        except:
            self.viewport=""

        try:
            self.faddress=self.data['results'][0]['formatted_address']
        except:
            self.faddress=""

        try:
            self.id=self.data['results'][0]['place_id']
        except:
            self.id=""

        UE_L=['ALLEMAGNE','AUTRICHE','BELGIQUE','BULGARIE','CHYPRE','DANEMARK','ESPAGNE','ESTONIE','FINLANDE','FRANCE','GRÈCE','HONGRIE','IRLANDE','ITALIE','LETTONIE','LITUANIE','LUXEMBOURG','MALTE','PAYS-BAS','POLOGNE','PORTUGAL','TCHÉQUIE','ROUMANIE','ROYAUME-UNI','SLOVAQUIE','SLOVÉNIE','SUÈDE']
        try:
            if self.country in UE_L:
                self.ue='UE'
            else:
                self.ue='NON UE'
        except:
            self.ue=''

from pointage import support as sp
import json
from urllib.parse import quote
import requests
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

class custom_search:
    def __init__(self,query):
        self.query = query
        self.url='https://customsearch.googleapis.com/customsearch/v1?cx=58ce1194b1c255cfb&q='+quote(self.query)+'&gl=fr&key=AIzaSyDHmj66uOLMdm25lPwg6amIrAxSmjdEm-o'
        self.tripadvisor=None
        self.hotels=None
        self.hrs=None
        self.elong=None
        self.agoda=None
    def request(self):
        global page
        global links
        links=[]
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36", 'referer':'https://www.google.com/' }
        http_proxy  = "http://127.0.0.1:24004"
        https_proxy = "https://127.0.0.1:24004"
        ftp_proxy   = "ftp://127.0.0.1:24004"

        proxyDict = {
                      "http"  : http_proxy,
                      "https" : https_proxy,
                      "ftp"   : ftp_proxy
                    }
        #add proxies if necessary

        page=requests.get(self.url,verify=False,headers=headers)
        csjson=json.loads(page.text)
        for item in csjson['items']:
            links.append(item['link'])
        temp_trip=[x for x in links if 'tripadvisor.fr' in x]
        temp_hotel=[x for x in links if 'fr.hotels.com' in x]
        temp_hrs=[x for x in links if 'hrs.com/fr' in x]
        temp_elong=[x for x in links if 'hotel.elong.com' in x]
        temp_agoda=[x for x in links if 'www.agoda.com/fr-fr/']

        try:
            trip_url=temp_trip[0]
        except:
            trip_url=""
        try:
            hotel_url=temp_hotel[0]
        except:
            hotel_url=""
        try:
            hrs_url=temp_hrs[0]
        except:
            hrs_url=""
        try:
            elong_url=temp_elong[0]
        except:
            elong_url=""
        try:
            agoda_url=temp_agoda[0]
        except:
            agoda_url=""
        self.tripadvisor=trip_url
        self.hotels=hotel_url
        self.hrs=hrs_url
        self.elong=elong_url
        self.agoda=agoda_url
        #return links

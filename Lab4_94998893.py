#Lawrence Byun
#94998893
import json
import urllib.parse
import urllib.request
consumerkey = 's6ut5J13905M87bCl67XTGz3jrDihKAC'
consumersecret = 'yNPoHMLjmCCaM92c'
class MapQuest:
    def __init__(self, key):
        self._key = key
    def totalDistance(self, locations: list) -> float:
        base = 'http://open.mapquestapi.com/directions/v2/route'
        if len(locations) > 1:
            distance = 0
            for i in range(len(locations) - 1):
                queryParameters = [('key', self._key),('from', locations[i]), ('to', locations[i + 1])]
                url = base + '?' + urllib.parse.urlencode(queryParameters)
                response = None
                try:
                    response = urllib.request.urlopen(url)
                    results = json.load(response)
                finally:
                    if response:
                        response.close()
                distance += results['route']['distance']
            return distance
        else:
            return 0

    def totalTime(self, locations: list) -> int:
        base = 'http://open.mapquestapi.com/directions/v2/route'
        if len(locations) > 1:
            time = 0
            for i in range(len(locations) - 1):
                queryParameters = [('from', locations[i]), ('to', locations[i + 1]), ('key', self._key)]
                url = base + '?' + urllib.parse.urlencode(queryParameters)
                response = None
                try:
                    response = urllib.request.urlopen(url)
                    results = json.load(response)
                finally:
                    if response:
                        response.close()
                time += results['route']['time']
            return time
        else:
            return 0

    def directions(self, locations: list) -> str:
        base = 'http://open.mapquestapi.com/directions/v2/route'
        if len(locations) > 1:
            direction = ''
            for i in range(len(locations) - 1):
                queryParameters = [('key', self._key),('from', locations[i]), ('to', locations[i + 1])]
                url = base + '?' + urllib.parse.urlencode(queryParameters)
                response = None
                try:
                    response = urllib.request.urlopen(url)
                    results = json.load(response)
                finally:
                    if response:
                        response.close()
                for i in range(len(results['route']['legs'][0]['maneuvers'])):
                    direction += results['route']['legs'][0]['maneuvers'][i]['narrative'] + '\n'         
            return direction
        else:
            return ''
    
    def pointOfInterest(self, locations: str, keyword: str, results: int) -> list:
        base = 'http://www.mapquestapi.com/search/v4/place'
        location = self.long_lat(locations)
        queryParameters = [('key', self._key), ('location', location), ('sort', 'distance'), ('limit', results), ('q', keyword)]
        url = base + '?' + urllib.parse.urlencode(queryParameters)
        response = None
        try:
            response = urllib.request.urlopen(url)
            info = json.load(response)
        finally:
            if response:
                response.close()
        lst = []
        for i in range(len(info['results'])):
            lst.append(info['results'][i]['displayString'])
        return lst

    def long_lat(self, locations: str):
        base = 'http://www.mapquestapi.com/geocoding/v1/address'
        queryParameters = [('key', self._key), ('location', locations)]
        url = base + '?' + urllib.parse.urlencode(queryParameters)
        response = None
        try:
            response = urllib.request.urlopen(url)
            results = json.load(response)
        finally:
            if response:
                response.close()
        latitude = results['results'][0]['locations'][0]['latLng']['lat']
        longitude = results['results'][0]['locations'][0]['latLng']['lng']
        longlat = str(longitude) + ',' + str(latitude)
        return longlat

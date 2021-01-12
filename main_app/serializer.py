import json

class Serializer:

    @staticmethod
    def format_coordiantes(info):
        return info['results'][0]['locations'][0]['latLng']

    @staticmethod
    def format_data(info):
        parks = []
        for park in info['results']:
            # code.interact(local=dict(globals(), **locals()))
            data = {
                'formatted_address': park['vicinity'],
                'geometry': park['geometry'],
                'name': park['name'],
                'opening_hours': park['opening_hours'] if 'opening_hours' in park else 'CLOSED',
                'photos': park['photos'] if 'photos' in park else 'NO PHOTOS',
                'rating': park['rating']}
            parks.append(data)
        return parks

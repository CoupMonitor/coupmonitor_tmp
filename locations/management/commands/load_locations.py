from django.core.management.base import BaseCommand
from locations.models import Location 
import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials
import os

class Command(BaseCommand):

    args = '<foo bar>'
    help = 'Load a list of locations into the database, the locations are loaded from the google sheet'

    
    def _load_locations(self):
	currpath = os.path.dirname(os.path.realpath(__file__))
	json_key = json.load(open(os.path.join(currpath, 'oauth.json')))
	scope = ['https://spreadsheets.google.com/feeds']

	ss_key = "1jq29zFTJQhAMF3DmYLH6_8uNJNWH_HOFGigk7HB7dS8"

	ws_name = "locations"

	credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
	gc = gspread.authorize(credentials)

	ss = gc.open_by_key(ss_key)

	ws = ss.worksheet(ws_name)

	all_values = ws.get_all_values()

	
	for value in all_values[1:]:
	    print(value)
	    try:
	        latitude = float(value[4])
	    except Exception:
	        latitude = None

	    try:
	        longitude = float(value[5])
	    except Exception:
	        longitude = None

	    l1 = Location.objects.language('ar').create(
		name= value[0],
		governorate=value[2],
		lat=latitude,
		lon=longitude,
	    )
            l1.translate('en')
            l1.name = value[1]
            l1.governorate = value[3]
	   

            l1.save()

 

    def handle(self, *args, **options):
        self._load_locations()

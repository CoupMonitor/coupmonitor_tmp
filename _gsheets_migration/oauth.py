import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials

email = "anon.r4bia@gmail.com"
json_key = json.load(open('oauth.json')) 
scope = ['https://spreadsheets.google.com/feeds']

ss_key = "1jq29zFTJQhAMF3DmYLH6_8uNJNWH_HOFGigk7HB7dS8"

ws_name = "locations"


credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

ss = gc.open_by_key(ss_key)

print 'i was here'
ws = ss.worksheet(ws_name)

#all_values = ws.get_all_values()

print( ws.row_values(1) )
print( ws.row_values(2) )






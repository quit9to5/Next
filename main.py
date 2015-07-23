import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import json
import time

SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "/tmp/a.json"
SPREADSHEET = "Patient Management (Responses)"

json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], SCOPE)
gc = gspread.authorize(credentials)
print("The following sheets are available")
for sheet in gc.openall():
    print("{} - {}".format(sheet.title, sheet.id))

while True:
	workbook = gc.open(SPREADSHEET)
	# Get the first sheet
	sheet = workbook.sheet1
	print sheet.get_all_records()
	time.sleep(0.1)

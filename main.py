import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import json
import time
import urllib2, urllib

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


def search_list_number(thelist, num):
	for i in thelist:
		if str(i['Mobile No']) == str(num):
			return 1
	return 0

def send_sms(num, msg):
	url="http://smslane.com/vendorsms/pushsms.aspx?user=quit9to5&password=720654&msisdn=919441354830&sid=WEBSMS&msg=I%20got%20your%20appointment&fl=0"
	response = urllib2.urlopen(url)
	html = response.read()
	print html

	
SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "./a.json"
SPREADSHEET = "Patient Management (Responses)"

json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], SCOPE)
gc = gspread.authorize(credentials)
print("The following sheets are available")
for sheet in gc.openall():
    print("{} - {}".format(sheet.title, sheet.id))

workbook = gc.open(SPREADSHEET)
sheet = workbook.sheet1
global_patient = sheet.get_all_records()
print global_patient
queue = Queue()


while True:
	# Get the first sheet
	sheet = workbook.sheet1
	for i in sheet.get_all_records():
		if not search_list_number(global_patient, i['Mobile No']):
			queue.enqueue(i)
			print "New patiend added", i
			global_patient.append(i)
			send_sms(i['Mobile No'], "test")
	print "queue size" + str( queue.size())
	
	time.sleep(0.1)

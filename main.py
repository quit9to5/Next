#!/usr/bin/python
from gdata.spreadsheet.service import SpreadsheetsService

key = '0Aip8Kl9b7wdidFBzRGpEZkhoUlVPaEg2X0F2YWtwYkE'

client = SpreadsheetsService()
feed = client.GetWorksheetsFeed(key, visibility='public', projection='basic')

for sheet in feed.entry:
  print sheet.title.text

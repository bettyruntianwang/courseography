from geopy.geocoders import Nominatim
import csv
import sqlite3

connection = sqlite3.connect('db/database.sqlite3')
connection.row_factory = sqlite3.Row

geolocator = Nominatim()

cursor = connection.cursor()
cursor.execute('SELECT * FROM building')

with open('/app/WebParsing/building.csv', 'w') as building_file:
  writer = csv.writer(building_file)
  writer.writerow(['code', 'name', 'address', 'postal_code', 'lat', 'lng'])
  for build in cursor:
    address = build['address'].split('(')[0]

    if "Queen's Park Crsc" in address:
      address = address.replace("Queen's Park Crsc", "Queen's Park Crescent")
      print(address)
    building_location = geolocator.geocode(address + ',Toronto, Ontario, Canada')

    writer.writerow([build['code'], build['name'], build['address'], build['postal_code'],\
      building_location.latitude, building_location.longitude])

    print(build['name'])

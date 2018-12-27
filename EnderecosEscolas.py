import requests
import os
import csv

os.chdir('C:/Users/rmaciel/Desktop/python')
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'


def buscaCoordenadas(local):
	params = {
	    'address': local,
	    'sensor': 'false',
	    'region': 'br',
	    'key' : 'INSERT YOUR KEY'
	}
	fl = []

	# Do the request and get the response data
	req = requests.get(GOOGLE_MAPS_API_URL, params=params)
	res = req.json()

	# Use the first result
	try:
		result = res['results'][0]
		geodata = dict()
		geodata['lat'] = result['geometry']['location']['lat']
		geodata['lng'] = result['geometry']['location']['lng']
		geodata['address'] = result['formatted_address']
		fl.append(geodata['address'])
		fl.append(geodata['lat'])
		fl.append(geodata['lng'])
	except IndexError:
		fl.append('não encontrado')
		fl.append(-15.7750837)
		fl.append(-48.0772769)
	finally:
		return fl
	
##abre o arquivo de escolas
with open ('Escolas3.csv', 'r', encoding='cp1252') as csvfile:
	baseEscolas = csv.reader(csvfile, delimiter = ';')
	for row in baseEscolas:
		busca = row[1] + ', '+row[2]+' - '+row[3]
		resultado = buscaCoordenadas(busca)
		arq = open('Escolas6.csv','a', encoding = 'UTF-'8)
		txt = row[0]+';'+row[1]+';'+row[2]+';'+row[3]+';'+str(resultado[1])+';'+str(resultado[2])+';'+resultado[0]+'\n'
		print(txt)
		arq.write(txt)
		arq.close()

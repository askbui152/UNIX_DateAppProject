# Date Night App with Python by James Bui, Quyen Mac, Justin Lu, Richard Ma
# for ECE 2524 Final Project 

import sys 
import urllib
import urllib2
import json
import argparse
import requests
import geocoder
import yelp
# Yelp API v2.0 key and token access 
yelp_consum_key = 'h87mQbOfy1oh2HsECVvFTw'
yelp_consum_secret = 'F-o0877jY6_yW39hU16ij4-YZ6g'
yelp_token = '7XaEjV0vRRT2esfa3NadQVQKB_-pPnRx'
yelp_token_secret = 'TNKA8qlMAKRcAkHn8oyYzs-8UWQ'

gmap_API_key = 'AIzaSyCX0kXtCU4lBw4VTxqRIOzajj9jDLqRNYU'
gmap_clientID = '141690507319-rrbbq0bffv3oj219fj9tq8d17svitk05.apps.googleusercontent.com'
gmap_clientSecret = 'QDGbuT59VlLT4GOyYDWqGbzd'

#def imdb or rotten tomatoes():

#def Google maps 
#def gmaps(start_latlng, end_latlng):
def gmaps():
	#link = 'https://maps.googleapis.com/maps/api/directions/json?origin='+'start_latlng'+'&destination='+'end_latlng'+'&key='+gmap_API_key
	link = 'https://maps.googleapis.com/maps/api/directions/json?origin=Chicago,IL&destination=Los+Angeles,CA&waypoints=Joplin,MO|Oklahoma+City,OK&key=AIzaSyCX0kXtCU4lBw4VTxqRIOzajj9jDLqRNYU'
	direction = requests.get(link)
	read_data = direction.text
	print read_data
	#for step in direction['Directions']['Routes'][0]['Steps']:
		#print step['descriptionHtml']
	#print 'did not work'

def use_yelp(category, address):
	yelp_api = yelp.Api(yelp_consum_key,yelp_consum_secret,yelp_token,yelp_token_secret)
	search_results = yelp_api.Search(term=category, location=address)
	for business in search_results.businesses:
		print business.name

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-a', action='store', dest='addr', help='Address')
	parser.add_argument('-c', action='store', dest='category', help='Food Category')
	parse_results = parser.parse_args()
	#use_yelp(parse_results.category,parse_results.addr)
	#gmaps('[38.819151, -77.201651]', '[37.2436, -80.4214]')
	gmaps()
	#print search_results.businesses.name[0]
	#yelp_business = yelp.Business(search_results.businesses[0])
	#print yelp_business.location


###TEST COMMIT


if __name__ == '__main__':
	main()


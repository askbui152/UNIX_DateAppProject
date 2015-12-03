# Date Night App with Python by James Bui, Quyen Mac, Justin Lu, Richard Ma
# for ECE 2524 Final Project 

import sys 
import urllib
import urllib2
import json
import argparse
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
#def yelp():

#def imdb or rotten tomatoes():

#def Google maps 

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-a', action='store', dest='addr', help='Address')
	parser.add_argument('-c', action='store', dest='category', help='Food Category')
	parse_results = parser.parse_args()
	yelp_api = yelp.Api(yelp_consum_key,yelp_consum_secret,yelp_token,yelp_token_secret)
	search_results = yelp_api.Search(term=parse_results.category, location=parse_results.addr)
	for business in search_results.businesses:
		print business.name
	#print search_results.businesses.name[0]
	#yelp_business = yelp.Business(search_results.businesses[0])
	#print yelp_business.location

if __name__ == '__main__':
	main()



# coding: utf-8

# In[7]:

from googleplaces import GooglePlaces, types, lang

API_KEY = 'AIzaSyDMqr9dX3u1ZVqnevh3SBy6qiVL0wBwJWE'

google_places = GooglePlaces(API_KEY)


# In[8]:

# You may prefer to use the text_search API, instead.
query_result = google_places.nearby_search(
        location='53.402577,-2.97676', radius=200, 
        types=[types.TYPE_TRAIN_STATION, types.TYPE_TAXI_STAND, types.TYPE_TRANSIT_STATION, 
               types.TYPE_AIRPORT, types.TYPE_SHOPPING_MALL]) #

# If types param contains only 1 item the request to Google Places API
# will be send as type param to fullfil:
# http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

if query_result.has_attributions:
    print (query_result.html_attributions)


# In[9]:

for place in query_result.places:
    # Returned places from a query are place summaries.
    print (place.name)
    print (place.types)
    #print (place.geo_location)
    #print (place.place_id)


# In[10]:

len(query_result.places)


# In[ ]:




# Import module
from geopy.geocoders import Nominatim
 
# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
 
# Assign Latitude & Longitude
 
# Displaying Latitude and Longitude
 
def get_location(lat, lon):
    location = geolocator.geocode(str(lat)+","+str(lon))
    return location
 
# Display location


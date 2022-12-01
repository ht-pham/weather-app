from google.cloud import firestore
from config import GOOGLE_APPLICATION_CREDENTIALS

# Create database instance / Connect to Firestore Client API for the Google Cloud project
database = firestore.Client(project=GOOGLE_APPLICATION_CREDENTIALS)

# Collection 'cities' for tracking all searched cities
cities_ref = database.collection('cities')
#default_city = cities_ref.document('default').set({"all visits":0})

# Collection 'web_visitors' for tracking number of users
web_visit_ref = database.collection('web_visitors')

def update_city(name):
    # Check if the city is already in the system
    city_ref = cities_ref.document(name).get()

    #city = city_ref.get()
        
    # If a document with ID name exists
    if city_ref.exists:
        current_data = city_ref.to_dict()
        current_data["lookup_count"] += 1 
        updated_data = current_data
        cities_ref.document(name).set(updated_data)  
    else:
        city_ref = cities_ref.document(name).set({"lookup_count":1})
        
def get_most_searched_city():
    cities = {}
    results = {}

    # Get data from database as a dict
    fs_stream = cities_ref.stream()
    for city in fs_stream:
        cities[city.id] = city.to_dict()

    # Get { city : #lookup }
    for city in list(cities.keys()):
        if city == 'default':
            continue
        results[city]= cities[city]["lookup_count"]
    
    most_looked_up = cities["default"]["lookup_count"]
    name = "default"
    for city in results.keys():
        if results[city] > most_looked_up:
            most_looked_up = results[city]
            name = city
    
    return name+" ("+str(most_looked_up)+" times)"

def update_visit_count():

    main_page = web_visit_ref.document('main_page').get().to_dict()
    main_page["visit_count"] += 1 
    web_visit_ref.document('main_page').set({"visit_count":main_page["visit_count"]})

def get_web_visitor_count():
    main_page_ref = web_visit_ref.document('main_page').get().to_dict()
    return main_page_ref["visit_count"]
    

        


    
    


    



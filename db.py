from google.cloud import firestore

database = firestore.Client(project="cloud-computing-fall22")

cities_ref = database.collection('cities') # Collection 'cities'
#default_city = cities_ref.document('default').set({"all visits":0})
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
        
        
def get_cities():
    cities = {}
    
    fs_stream = cities_ref.stream()
    for city in fs_stream:
        cities[city.id] = city.to_dict()

    return list(cities.keys())

def update_visit_count():

    main_page = web_visit_ref.document('main_page').get().to_dict()
    main_page["visit_count"] += 1 
    web_visit_ref.document('main_page').update({"visit_count":main_page["visit_count"]})
    

        


    
    


    



from flask import Flask
from flask import render_template
from flask import request as form

import requests
import json
import re 
app = Flask(__name__,template_folder="templates")

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/search",methods=["POST"])
def search():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    
    city = form.form["city"]
    querystring = {"q":city}
    
    headers = {
        "X-RapidAPI-Key": "153f94ba4amsh2b77e486cbac9e4p18bfaejsn63e24918a3ba",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }   

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    
    condition = json_data["current"]["condition"]["text"] # e.g. cloudy, sunny, foggy, etc.
    temp = {"C":json_data["current"]["temp_c"],"F":json_data["current"]["temp_f"],
                    "Real-Feel C":json_data["current"]["feelslike_c"],"Real-Feel F":json_data["current"]["feelslike_f"]}
    wind = {"degree":json_data["current"]["wind_degree"],"dir":json_data["current"]["wind_dir"],
            "speed_kph":json_data["current"]["wind_kph"],"speed_mph":json_data["current"]["wind_mph"]}

    """ # This is future use to the database
    with open("templates/location.html","w") as page:
        for line in page:
            if not re.findall("</p>",line):
                continue
            else:
                page.write(display_output)
    
    page.close() 
    """
    return render_template("location.html",var1=city,var2=condition,var3=temp["C"],var4=temp["F"],
            var5=temp["Real-Feel C"],var6=temp["Real-Feel F"],var7=wind["degree"],var8=wind["dir"],
            var9=wind["speed_kph"],var10=wind["speed_mph"])
    

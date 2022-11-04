from flask import Flask
from flask import render_template
from flask import request as form

import requests
import json
import re 
app = Flask(__name__,template_folder="templates")

@app.route("/")
def main_page():
    return render_template("index.html",var1="")

@app.route("/search",methods=["POST"])
def search():
    url_current = "https://weatherapi-com.p.rapidapi.com/current.json"
    url_astronomy = "https://weatherapi-com.p.rapidapi.com/astronomy.json"

    city = form.form["city"]
    # Exception Handling: Empty Input ==> Refresh Main Page
    if city == "":
        return render_template("index.html",var1="Please enter a city")

    querystring = {"q":city}
    
    headers = {
        "X-RapidAPI-Key": "153f94ba4amsh2b77e486cbac9e4p18bfaejsn63e24918a3ba",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }   

    response_current = requests.request("GET", url_current, headers=headers, params=querystring)
    current_data = json.loads(response_current.text)

    # When the user gives an unvalid input other than empty string
    # i.e. 4xx Error 
    if (response_current.status_code in range(400,500)):
        return render_template("index.html",var1="No Matching Found Location")
    # When some codes are not working properly
    # i.e. 5xx Error
    elif (response_current.status_code in range(500,600)):
        return render_template("error.html",var1=response_current.status_code,var2=response_current.reason)
    
    response_astronomy = requests.request("GET", url_astronomy, headers=headers, params=querystring)
    astro_data = json.loads(response_astronomy.text)

    city = current_data["location"]["name"]+", "+current_data["location"]["region"]
    time = current_data["location"]["localtime"]
    sunrise = astro_data["astronomy"]["astro"]["sunrise"]
    sunset = astro_data["astronomy"]["astro"]["sunset"]

    condition = current_data["current"]["condition"]["text"] # e.g. cloudy, sunny, foggy, etc.
    temp = {"C":current_data["current"]["temp_c"],"F":current_data["current"]["temp_f"],
                    "Real-Feel C":current_data["current"]["feelslike_c"],"Real-Feel F":current_data["current"]["feelslike_f"]}
    wind = {"degree":current_data["current"]["wind_degree"],"dir":current_data["current"]["wind_dir"],
            "speed_kph":current_data["current"]["wind_kph"],"speed_mph":current_data["current"]["wind_mph"]}

    """ # This is future use to the database
    with open("templates/location.html","w") as page:
        for line in page:
            if not re.findall("</p>",line):
                continue
            else:
                page.write(display_output)
    
    page.close() 
    """
    return render_template("location.html",var1=city,
            time=time,sunrise=sunrise,sunset=sunset,
            var2=condition,var3=temp["C"],var4=temp["F"],
            var5=temp["Real-Feel C"],var6=temp["Real-Feel F"],
            var7=wind["degree"],var8=wind["dir"],
            var9=wind["speed_kph"],var10=wind["speed_mph"])
    

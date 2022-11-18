from flask import Flask
from flask import render_template
from flask import request as form

import requests
import json
import re 
app = Flask(__name__,template_folder="templates")

@app.route("/")
def main_page():
    return render_template("index.html",error_message="")

@app.route("/search",methods=["POST"])
def search():
    # Take user input and save it as the variable 'city'
    city = form.form["city"]

    # Exception Handling: Empty Input ==> Refresh Main Page
    if city == "":
        return render_template("index.html",error_message="Please enter a city")
        
    
    if(form.form["action"]=="now"):

        # URLs for HTTP POST requests
        url_current = "https://weatherapi-com.p.rapidapi.com/current.json"
        url_astronomy = "https://weatherapi-com.p.rapidapi.com/astronomy.json"

        # Headers info { API key & and API host } to make API calls
        headers = {
            "X-RapidAPI-Key": "153f94ba4amsh2b77e486cbac9e4p18bfaejsn63e24918a3ba",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }   
        # Otherwise, take the entered user input 'city' to the query
        querystring = {"q":city}

        # First API call for the real-time weather info in the city
        response_current = requests.request("GET", url_current, headers=headers, params=querystring)
        current_data = json.loads(response_current.text)
        # Second API call for the astronomy info of the city (i.e. sunrise and sunset time)
        response_astronomy = requests.request("GET", url_astronomy, headers=headers, params=querystring)
        astro_data = json.loads(response_astronomy.text)

        # Exception Handling: invalid user input
        # When the user gives an unvalid input other than empty string
        # return 4xx Error 
        if (response_current.status_code in range(400,500)):
            return render_template("index.html",error_message="No Matching Found Location")
        
        # Exception Handling: buggy codes/internal server issues
        # When some codes are not working properly
        # return 5xx Error
        if (response_current.status_code in range(500,600)):
            return render_template("error.html",status_code=response_current.status_code,error_message=response_current.reason)
        
        # Otherwise (i.e. it is a valid input which is a city/town), return the info
        if current_data["location"]["region"] == "" or current_data["location"]["region"] == current_data["location"]["name"] :
            city = current_data["location"]["name"]+", "+current_data["location"]["country"]
        else:
            city = current_data["location"]["name"]+", "+current_data["location"]["region"]
        time = current_data["location"]["localtime"]
        sunrise = astro_data["astronomy"]["astro"]["sunrise"]
        sunset = astro_data["astronomy"]["astro"]["sunset"]

        condition = current_data["current"]["condition"]["text"] # e.g. cloudy, sunny, foggy, etc.
        temp = {"C":current_data["current"]["temp_c"],"F":current_data["current"]["temp_f"],
                        "Real-Feel C":current_data["current"]["feelslike_c"],"Real-Feel F":current_data["current"]["feelslike_f"]}
        wind = {"degree":current_data["current"]["wind_degree"],"dir":current_data["current"]["wind_dir"],
                "speed_kph":current_data["current"]["wind_kph"],"speed_mph":current_data["current"]["wind_mph"]}

        return render_template("location.html",location=city,
                time=time,sunrise=sunrise,sunset=sunset,
                desc=condition,celsius=temp["C"],fahrenheit=temp["F"],
                realfeel_c=temp["Real-Feel C"],realfeel_f=temp["Real-Feel F"],
                degree=wind["degree"],direction=wind["dir"],
                kmh=wind["speed_kph"],mph=wind["speed_mph"])

    elif (form.form["action"]=="forecast"):
        # URLs for HTTP POST requests
        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

        # Headers info { API key & and API host } to make API calls
        headers = {
            "X-RapidAPI-Key": "153f94ba4amsh2b77e486cbac9e4p18bfaejsn63e24918a3ba",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }   

        # Otherwise, take the entered user input 'city' to the query
        querystring = {"q":city,"days":"3"}

        # First API call for the real-time weather info in the city
        forecast_response = requests.request("GET", url, headers=headers, params=querystring)
        forecast_data = json.loads(forecast_response.text)

        # Exception Handling: invalid user input
        # When the user gives an unvalid input other than empty string
        # return 4xx Error 
        if (forecast_response.status_code in range(400,500)):
            return render_template("index.html",error_message="No Matching Found Location")
        
        # Exception Handling: buggy codes/internal server issues
        # When some codes are not working properly
        # return 5xx Error
        if (forecast_response.status_code in range(500,600)):
            return render_template("error.html",status_code=forecast_response.status_code,error_message=forecast_response.reason)
        
        tomorrow = str(forecast_data["forecast"]["forecastday"][1]["date"])
        tomorrow_data = forecast_data["forecast"]["forecastday"][1]["day"]
        tomorrow_astro = forecast_data["forecast"]["forecastday"][1]["astro"]

        return tomorrow+"\n"+str(tomorrow_data["maxtemp_f"])+"\n"+str(tomorrow_data["mintemp_f"])+"\n"+str(tomorrow_astro["sunrise"])


@app.route("/forecast",methods=["POST"])
def forecast():
    # URLs for HTTP POST requests
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    # Headers info { API key & and API host } to make API calls
    headers = {
        "X-RapidAPI-Key": "153f94ba4amsh2b77e486cbac9e4p18bfaejsn63e24918a3ba",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }   

    # Take user input and save it as the variable 'city'
    city = form.form["city"]

    # Exception Handling: Empty Input ==> Refresh Main Page
    if city == "":
        return render_template("index.html",error_message="Please enter a city")
    
    # Otherwise, take the entered user input 'city' to the query
    querystring = {"q":city,"days":"3"}

    # First API call for the real-time weather info in the city
    forecast_response = requests.request("GET", url, headers=headers, params=querystring)
    forecast_data = json.loads(forecast_response.text)

    # Exception Handling: invalid user input
    # When the user gives an unvalid input other than empty string
    # return 4xx Error 
    if (forecast_response.status_code in range(400,500)):
        return render_template("index.html",error_message="No Matching Found Location")
    
    # Exception Handling: buggy codes/internal server issues
    # When some codes are not working properly
    # return 5xx Error
    if (forecast_response.status_code in range(500,600)):
        return render_template("error.html",status_code=forecast_response.status_code,error_message=forecast_response.reason)
    
    
    tomorrow = str(forecast_data["forecast"]["forecastday"][1]["date"])
    tomorrow_data = forecast_data["forecast"]["forecastday"][1]["day"]
    tomorrow_astro = forecast_data["forecast"]["forecastday"][1]["astro"]

    return tomorrow+"\n"+str(tomorrow_data["maxtemp_f"])+"\n"+str(tomorrow_data["mintemp_f"])+"\n"+str(tomorrow_astro["sunrise"])
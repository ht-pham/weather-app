# Weather App
## Overview
This is a final project for UTSA CS5573 Cloud Computing course in Fall 2022. The project is built in Python with Flask framework and deployed by Google AppEngine. The web app is also capable of collecting metrics to perform statistics (i.e. number of times the web app was visited, and the most searched city for the weather forecast functions) by being connected to Google Cloud Firestore to which it automatically data and from which it gets data. The public URL for this application is [here](https://cloud-computing-fall22.uc.r.appspot.com).
## Structure of the project
1. app.yaml: the configuration file for Google AppEngine Deployment
2. 'static' folder: where JS and CSS files are saved
3. 'templates' folder: where all .html files are saved
4. requirements.txt: the list of required framework/library and their versions to run this application on local host.
5. main.py: the Flask application
6. db.py: the Firestore database module
## Software Requirements
1. Python 3.9+ or any latest version (see [link](https://www.python.org/downloads/) for lastest download)
2. 'requests' module: for API calls\
3. Flask framework
4. Google Cloud Firestore API

#### Option 1: Install the required packages to virtual environment only
- Step 1: Create a virtual environment
```
$ mkdir your-local-repo
$ cd your-local-repo
$ python3 -m venv venv
```
- Step 2: Activate your virtual environment\
```$ .venv/bin/activate```
- Step 3: Install Flask onto the virtual environment\
```$ pip install -r requirements.txt```



#### Option 2: Install the required packages to your local machine
In your terminal/cmd prompt, run 
```
$ pip install Flask
$ pip install requests
$ pip install google-cloud-firestore
```

## How to Run the project
### Download the project
In your terminal/cmd prompt, run ```git clone https://github.com/ht-pham/weather-app.git```
### How to Run the Application
#### Option 1: On a Virtual Environment
In your terminal/cmd prompt:
```
local-repo$ .venv/bin/activate
local-repo$ pip install -r requirements.txt
local-repo$ flask --app main run
```
#### Option 2: On your machine
After installing the required packages (Flask,requests, and google-cloud-firestore), in terminal:
1. Change directory to where 'main.py' is located: ```$ cd your-local-repo```
2. Run the program: ```your-local-repo$ flask --app main run```
## Acknowledgement
Thank you to @RapidAPI for the free subcription for [weather api](https://rapidapi.com/weatherapi/api/weatherapi-com/).


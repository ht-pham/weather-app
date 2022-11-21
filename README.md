# Weather App
## Overview
This is a final project for UTSA CS5573 Cloud Computing course in Fall 2022. The project is built in Python with Flask framework and deployed by Google AppEngine. The public URL for this application is [here](https://cloud-computing-fall22.uc.r.appspot.com).
## Structure of the project
1. app.yaml: the configuration file for Google AppEngine Deployment
2. 'static' folder: where JS and CSS files are saved
3. 'templates' folder: where all .html files are saved
4. requirements.txt: the list of required framework/library to run this application on local host.
5. main.py: the Flask application
## Software Requirements
1. Python 3.7+ or any latest version (see [link](https://www.python.org/downloads/) for lastest download)
2. Flask framework: 
#### Option 1: Flask installation on a virtual environment
- Step 1: Create a virtual environment
```
$ mkdir your-local-repo
$ cd your-local-repo
$ python3 -m venv venv
```
- Step 2: Activate your virtual environment\
```$ .venv/bin/activate```
- Step 3: Install Flask onto the virtual environment\
```pip install Flask```
\
**Note**: you will have to repeat the steps 2 and 3 every time you want to run the project
#### Option 2: Flask installation on your machine
In your terminal/cmd prompt, run ```pip install Flask```
## How to Run the project
### Download the project
In your terminal/cmd prompt, run ```git clone https://github.com/ht-pham/weather-app.git```
### How to Run the Application
#### Option 1: On a Virtual Environment
In your terminal/cmd prompt:
1. Repeat step 2 and step 3 in Flask installation on a virtual environment
2. Run ```flask --app main run```
#### Option 2: On your machine
In terminal:
1. Change directory to where 'main.py' is located: ```$ cd your-local-repo```
2. Run the program: ```your-local-repo$ flask --app main run```
## Acknowledgement
Thank you to @RapidAPI for the free subcription for [weather api](https://rapidapi.com/weatherapi/api/weatherapi-com/).


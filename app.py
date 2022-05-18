#App file to define app routes

# first in terminal in my working dir for this session run =
# $  pip3 install mysql-connector-python   (or try pip or -m pip...)

# now make sure we have the library     mysql-connector-python    pip installed!
    # run 'python -m pip list' from the terminal to check your installed libraries
    # import using pip if needed, use :  -m pip install mysql-connector-python

# The below should not be needed, but keep in mind if error occurs =
# first install flask via command line =
 # $ pip3 install flask
 # $ pip3 install jsonify
 # $ pip3 install requests

from flask import Flask, jsonify

from db_utils import (get_country, show_cities, show_cities_and_weather,
                      show_essential_items, show_months, show_personal_items)

app = Flask(__name__)

@app.route('/travel/months/', methods=['GET'])
def app_get_month_choices():
    res = show_months()
    return jsonify(res)

    # Generates this URL =
        #http://127.0.0.1:5001/travel/months/


##  GET TOP 8 EUROPEAN DESTINATIONS FOR SUMMER HOLIDAYS
@app.route('/travel/cities/', methods=['GET'])
def app_get_cities():
    res = show_cities()
    return jsonify(res)

    #http://127.0.0.1:5001/travel/cities/


##  GET WEATHER FOR TOP 8 EUROPEAN DESTINATIONS FOR SELECTED MONTH
@app.route('/travel/cities-weather-month/<month>', methods=['GET'])
def app_get_city_weather(month):
    res = show_cities_and_weather(month)
    return jsonify(res)

    #http://127.0.0.1:5001/travel/cities-weather-month/

    # Example: http://127.0.0.1:5001/travel/cities-weather-month/July


##  GET ESSENTIAL ITEMS FOR SELECTED MONTH AND DESTINATION
@app.route('/travel/essential-items/<month>/<city>', methods=['GET'])  # generates the endpoint at an specific URl
def app_get_essential_items(month, city):
    res = show_essential_items(month, city)
    return jsonify(res)

    # http://127.0.0.1:5001/travel/essential-items/month/city
    # Example: http://127.0.0.1:5001/travel/essential-items/July/Paris



# GET PERSONAL ITEMS NEEDED FOR TRIP
@app.route('/travel/personal-items/', methods=['GET'])
def app_get_personal_items():
    res = show_personal_items()
    return jsonify(res)

    #http://127.0.0.1:5001/travel/personal-items/



if __name__ == '__main__':
    app.run(debug=True, port=5001)

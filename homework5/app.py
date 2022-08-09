from flask import Flask, request
import redis
import json
import logging

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def data():

    """
    
    data retrieval/input method for the Flask application.
    A POST request to /data loads some Meteorite Landings data into your Redis database instance
    A GET request to /data reads the data out of Redis and returns it as a JSON list

    Args:
        None
    
    Returns:

    GET: ML_data: a JSON list of meteorite landing data from the Redis database
    POST: A string indicating the data was committed to the redis database

    """

    red = redis.Redis(host = "172.17.0.3", port = 6425, db = 25)

    ml_data = {}

    if request.method == 'POST':

        logging.info("loading files into redis")
        
        with open('ML_Data_Sample.json', 'r') as f:
            ml_data = json.load(f)

        red.set("ml_data", json.dumps(ml_data['meteorite_landings']))
        return "data loaded into database"
       
    else:
        
        logging.info("retrieving data from redis")

        tempdata = []

        for i in ml_data['meteorite_landings']:
            tempdata.append(json.loads(red.get(i)))

        ML_data = json.dumps(tempdata, indent = 2)

        return ML_data

if __name__ == "__main__": 
    app.run(debug = True, host = '0.0.0.0')


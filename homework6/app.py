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

    red = redis.Redis(host = "172.17.0.2", port = 6379, db = 0)

    global ml_data

    if request.method == 'POST':

        logging.info("loading files into redis")
        
        with open('ML_Data_Sample.json', 'r') as f:
            ml_data = json.load(f)

        for i in ml_data['meteorite_landings']:
            red.set(i,json.dumps(i))

        return "data loaded into database\n"
       
    else:
        
        logging.info("retrieving data from redis")

        tempdata = []

        for i in ml_data:
            tempdata.append(json.loads(red.get(i)))

        finaldata = json.dumps(tempdata, indent = 2)

        return finaldata

if __name__ == "__main__":

    with open('ML_Data_Sample.json', 'r') as f:
        ml_data = json.load(f)
        
   #app.run(debug = True, host = '0.0.0.0')


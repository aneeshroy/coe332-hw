# Homework 5: Back to the Flask

## Overview

In this short homework assignment, it contains instructions to launch a Redis container, then use a small Flask app to load data into and retrieve data from the database.

## Files

the files in this project are `app.py` hosting the app scripts and routes, `Dockerfile` to build and containerize the application, and this README. the dataset `ml_data_sample` can be downloaded through this command:

```
wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

## Instructions

To start the container, you can either download the finished container through

```
docker pull aneeshroy/ml_data_redis:1.0
```

Or build your own container image through the Dockerfile by inputting

```
docker build -t aneeshroy/ml_data_redis:1.0 .
```

replacing the username with your own. After this, we need to initialize the Redis server to ensure that the program can run smoothly. To do this, input

```
docker run -v $(pwd)/data:/data -d -p 6425:6379 --name=aneesh-redis redis:6 --save 1 1
```

You can replace your name and the port you are using as well to your own settings. After this, you can run the Flask application by inputting

```
docker run --rm -d --name=aneesh-flask aneeshroy/ml_data_redis:1.0
```

The flask should be up and running now. to run commands, first input 

```
curl localhost:5000/data -X POST
```
to load the data into the redis server. From here, you can the command again minus the `-X POST` to see the data in JSON format.

## Example Data

```
    {
      "name": "Gerald",
      "id": "10001",
      "recclass": "H4",
      "mass (g)": "5754",
      "reclat": "-75.6691",
      "reclong": "60.6936",
      "GeoLocation": "(-75.6691, 60.6936)"
    },
    {
      "name": "Dominique",
      "id": "10002",
      "recclass": "L6",
      "mass (g)": "1701",
      "reclat": "-9.4378",
      "reclong": "49.5751",
      "GeoLocation": "(-9.4378, 49.5751)"
    },
```



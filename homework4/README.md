# Homework 4: Once Upon a Time in Containers

## Description
The purpose of this project is to develop a full application that can be utilized by anyone through Docker Hub.

## ml_data_analysis.py Description
This python script's purpose is to read in a JSON file of meteorite landings and use several functions to 

1. Compute the average mass
2. check in which quadrant of the planet the object landed in
3. It counts how many meteorites land of each different composition
4. Output the results in a formatted fashion.

THe output looks like this:
```python
Summary data following meteorite analysis:

Average mass of 30 meteor(s): 83857.3 

Hemisphere summary data:
There were 6  meteors found in the  Northern & Western Quadrant.
There were 21  meteors found in the  Northern & Eastern Quadrant.
There were 3  meteors found in the  Southern & Western Quadrant.
There were 0  meteors found in the  Eastern & Western Quadrant.

Class summary data:
The   L5  class was found  1 times.
The   H6  class was found  1 times.
The   EH4  class was found  2 times.
The   Acapulcoite  class was found  1 times.
The   L6  class was found  6 times.
The   LL3-6  class was found  1 times.
The   H5  class was found  3 times.
The   L  class was found  2 times.
The   Diogenite-pm  class was found  1 times.
The   Stone-uncl  class was found  1 times.
The   H4  class was found  2 times.
The   H  class was found  1 times.
The   Iron-IVA  class was found  1 times.
The   CR2-an  class was found  1 times.
The   LL5  class was found  2 times.
The   CI1  class was found  1 times.
The   L/LL4  class was found  1 times.
The   Eucrite-mmict  class was found  1 times.
The   CV3  class was found  1 times.
```

## test_ml_data_analysis.py Description
This second Python Script is used to test the functions in the previous file through Pytest, as seen in previous homeworks.


## Meteorite_Landings.json Description
This is the data file used for the scripts, where the JSON file is formatted to contain all of the parameters necessary for the function.
A JSON formatted file is essentially a list of dictionaries

## Dockerfile
The Dockerfile is a set of instructions given to the machine to create a copy of the folder onto Docker Hub for use by others who wish to use the application.

Using docker to access this application can be done through the following:

## Instructions:

### Pull the image on Docker Hub 
1. Go to my Dockerhub profile
https://hub.docker.com/repository/docker/aneeshroy/ml_data_analysis

2. Use the version tagged `hw04`. You can pull this to your machine through the following command
```python
docker pull aneeshroy/ml_data_analysis:hw04
```

3.  Next, start the interactive shell:
```python
docker run --rm -it aneeshroy/ml_data_analysis:hw04 /bin/bash
```

4.  move into the file with the code:
```python
cd code
```

5. You can now run the code appropriately: 
```python
python3 ml_data_analysis.py Meteorite_Landings.json
```

### Build an image from your Dockerfile

1. Paste the following into the terminal. Replace the <username> with your username and <tag> with whatever tag you want.
```python
docker build -t <username>/ml_data_analysis:<tag> .
```

2.  Paste the following into the terminal. Replace the <username> with your username and <tag> with whatever tag you want.
```python
docker run --rm -it <username>/ml_data_analysis:<tag> /bin/bash
```

### Run the containerized code against the sample data inside the container 
    
1.  move into the file with the code:
```python
cd code
```
2. The code, assuming other steps have been done correctly, can be used appropriately now:
```python
python3 ml_data_analysis.py Meteorite_Landings.json
```

## Run the containerized code against user-provided data that they may have found on the web <a name="paragraph2"></a>
    
1.  Assuming you are in your own image when beginning, you can use you own data using the wget command: 
```python
wget https://<your_webstite_url_here>.com
```  
    
2. Next, start the interactive shell by running the following:
```python
docker run --rm -it -v $PWD:/data <username>/ml_data_analysis:<your_tag> /bin/bash
```

3.  move into the file with the code:
```python
cd code
```

4. YOu can use the code now, replacing the <filename> with the name you have imported from online.
```python
python3 ml_data_analysis.py <filename>.json
```


### Run the containerized test suite with pytest
    
1. While in your image of the application: run the following:
```python
pytest
```

### What input should look like

The input file should match the format of the `Meteorite_Landings.json` file from the application:

```python
{
    "name": "Wills",
    "id": "10017",
    "recclass": "Iron-IVA",
    "mass (g)": "50000",
    "reclat": "39.91667",
    "reclong": "42.81667",
    "GeoLocation": "(39.91667, 42.81667)"
}
```

There is additional meteorite landing data included through this [link.](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json)

use the instructions above to import this data into your own container and run the program.
    
    
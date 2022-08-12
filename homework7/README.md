
# Million Dollar Diagram: Application Structural Visualization

##Description

This homework houses a diagram that explains the routes a user can take in another project of mine, [O ISS, Where Art Thou?](https://github.com/aneeshroy/o-iss-where-art-thou)

The diagram can be found as the other file in this folder. It consists of the name of the project and a tagline describing it in a rudimentary fashion. Then it lists the files present in the repo ( `app.py`, `test_app.py`, `Dockerfile`, and `Makefile`. Then the next part below is a collection og the methods from app.py that a use can interact with using the Flask application. They are separated into the `GET` and `POST` methods. On the `POST` side, only the `/load_data` is there, which is used to load data into the Flask environment. The `GET` side contains the rest of the methods. If a method can only be reached by sequentially completing methods above, that is also shown. For the `epoch` sequence, there are only two, the epochs and the information about a specific epoch. for the `countries` sequence, a user can get to a country, region, and specific information about a city. The `/help` route only displays the rest of the commands.
 

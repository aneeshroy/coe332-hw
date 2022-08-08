FROM python:3.9

RUN mkdir /app
WORKDIR /app

RUN pip3 install Flask==2.0.3 \
                 redis   

COPY app.py /data/app.py
COPY ML_Data_Sample.json /data/ML_Data_Sample.json

ENTRYPOINT ["python"]
CMD ["app.py"]
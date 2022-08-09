FROM python:3.9

RUN mkdir /data
WORKDIR /data
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /data
COPY ML_Data_Sample.json /data/ML_Data_Sample.json

ENTRYPOINT ["python"]
CMD ["app.py"]

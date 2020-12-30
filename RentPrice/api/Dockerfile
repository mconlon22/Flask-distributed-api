FROM python:3.8-buster

WORKDIR /app
COPY . /app

# We copy just the requirements.txt first to leverage Docker cache
RUN apt-get update

RUN pip install --upgrade pip
COPY requirements.txt ./ 
RUN pip install -r requirements.txt


CMD ["python","RentPriceApi.py"]
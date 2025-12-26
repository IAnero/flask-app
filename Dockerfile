# specifying the base image, since this app is in python the base iamge will be python 
FROM python:3.8

# set an active to where we will copy the files of our app
WORKDIR /usr/src/app

COPY . .

# install dependacies, since it is in the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# to expose the port number, since flask use 5000 by default
EXPOSE 5000

# command to run the app when the docker will start
CMD ["python", "./app.py"]


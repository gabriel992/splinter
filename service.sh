#!/bin/bash

sudo docker build -t gabriel/flask-api:latest .

sudo docker run  -d --name api -p 5000:5000 gabriel/flask-api:latest
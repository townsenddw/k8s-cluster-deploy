#!/bin/python3

from csv import reader
import boto3
import requests

# curl http://schedules.calpoly.edu/csv/csm-jupyter.csv | cut -d',' -f1-9,13-17 

# Get File from Web URL="http://schedules.calpoly.edu/csv/csm-jupyter.csv"
url = 'http://schedules.calpoly.edu/csv/csm-jupyter.csv'
r = requests.get(url)

# Parse data (csv)

# Extract Capacity, StartTime, EndTime

# Generate Estimated need curve hourly (ie sum up enrolled per hour x gb-rm/user)

# Create scheduled scaling operations to match need curve
asc = boto3.client('autoscaling')
response = asc.describe_auto_scaling_groups()
print(response)

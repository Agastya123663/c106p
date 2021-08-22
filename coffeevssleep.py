import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
  coffee = []
  sleep = []
  with open(data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      coffee.append(float(row["Coffee in ml"]))
      sleep.append(float(row["sleep in hours"]))
  return{"x":coffee,"y":sleep}

def findCorrelation(data_source):
  correlation = np.corrcoef(data_source["x"],data_source["y"])
  print("correlation between coffee and sleep : ",correlation[0,1])

def setUp():
  data_path = "coffeevssleep.csv"
  data_source = getDataSource(data_path)
  findCorrelation(data_source)

setUp()


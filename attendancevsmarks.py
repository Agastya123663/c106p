import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
  marks = []
  attendance = []
  with open(data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      marks.append(float(row["Marks In Percentage"]))
      attendance.append(float(row["Days Present"]))
  return{"x":attendance,"y":marks}

def findCorrelation(data_source):
  correlation = np.corrcoef(data_source["x"],data_source["y"])
  print("correlation between attendance and marks : ",correlation[0,1])

def setUp():
  data_path = "attendancevsmarks.csv"
  data_source = getDataSource(data_path)
  findCorrelation(data_source)

setUp()


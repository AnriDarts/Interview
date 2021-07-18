import requests
import csv
import pandas as pd
import json

count = 10

jokes = []

url = "https://api.chucknorris.io/jokes/random"
file1 = open("data.txt", "w")

for i in range(count):
    response = requests.request("GET", url)
    data = response.text
    file1.write(data + "\n")

# \n is placed to indicate EOL (End of Line)
file1.close()


import pandas as pd
import json


# Reading the CSV file
df = pd.read_csv('./data/user.csv')

print(df.head())

# Converting the CSV to a JSON file
def convert_json(csvFilePath, jsonFilePath):

    data = {}

    

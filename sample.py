import pandas as pd
import json 

# .....reading json file named data.json......
event_data = pd.read_json("data.json")

# print(event_data)
# print(type(event_data))
# print(event_data.info())

# converting into excel file
# event_data.to_excel("convert_excel.xlsx", index=False)

# converting into csv file
event_data.to_csv("convert_csv.csv", index=False)

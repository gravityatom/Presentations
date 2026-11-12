#converting JSON file to CSV
"""
Created on Thu Nov 12 02:35:16 2026

@author: atom
"""
import sys
import json

json_file = r'C:\data\atom\nasa_app\neo_ws_20261105_to_20261112.json'


with open(json_file, "r", encoding="utf-8") as file:
    data = json.load(file)
   

csv_headers = [
'id',
'name',
'close_approach_date',
'miss_distance_km',
'relative_velocity_kph',
'estimated_diameter_min_km',
'estimated_diameter_max_km',
'is_potentially_harzardous',
'orbiting_body'
]

csv_content = [','.join(csv_headers)]

print(f"{csv_content}")
print(f"count: {len(csv_content)}")

sql_values = []    
for neo_date in data['near_earth_objects']:
    for date_item in data['near_earth_objects'][neo_date]:
       
        is_hazardous = 1 if f"{date_item['is_potentially_hazardous_asteroid']}" == 'True' else 0
       
        ## Remove open and close prentheses
        item_name = f"{date_item['name']}"
        item_name = item_name.replace('(', '')
        item_name = item_name.replace(')', '')
       
        row_item = ','.join([
            f"{date_item['id']}",
            f"'{item_name}'",
            f"{date_item['close_approach_data'][0]['close_approach_date']}",
            f"{date_item['close_approach_data'][0]['miss_distance']['kilometers']}",
            f"{date_item['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']}",
            f"{date_item['estimated_diameter']['kilometers']['estimated_diameter_min']}",
            f"{date_item['estimated_diameter']['kilometers']['estimated_diameter_max']}",
            f"{is_hazardous}",
            f"'{date_item['close_approach_data'][0]['orbiting_body']}'",
        ])
       
       
        csv_content.append(row_item)
        sql_values.append(row_item)

csv_file = json_file.replace('json','csv')
with open(csv_file, 'w') as csvfile:
    csvfile.write("\n".join(csv_content))

print(f"{csv_file} saved")

## Create SQL insert commands to import the data

column_names = ','.join(csv_headers)
sql_content  = [f"INSERT INTO near_earth_objects ({column_names})", "VALUES"]
for sql_value in sql_values:
    sql_content.append(f"({sql_value}),")



sql_file = json_file.replace('json','sql')
with open(sql_file, 'w') as sqlfile:
    sqlfile.write("\n".join(sql_content))

print(f"{sql_file} saved")

/*Create Table SQL statement*/
CREATE TABLE near_earth_objects (id INTEGER PRIMARY KEY, 
  name TEXT, 
  close_approach_date TEXT, 
  miss_distance_km REAL, 
  relative_velocity_kph REAL,
  estimated_diameter_min_km REAL, 
  estimated_diameter_max_km REAL, 
  is_potentially_harzardous INTEGER, 
  orbiting_body TEXT);




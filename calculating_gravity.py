import csv
import pandas as pd 
planet_mass=[]
planet_radii=[]
planet_names=[]

df = pd.read_csv('main.csv')

for planet_data in df:
    planet_mass.append(planet_data[2])
    planet_radii.append(planet_data[3])
    planet_names.append(planet_data[1])

  
df = pd.read_csv('main.csv')

planet_gravity=[]
for index,name in enumerate(planet_names):
    gravity = (float(planet_mass[index])*1.989e+30) / (float(planet_radii[index])*float(planet_radii[index])*6371000*6371000) * 6.957e+8
    planet_gravity.append(gravity)
    print(gravity)
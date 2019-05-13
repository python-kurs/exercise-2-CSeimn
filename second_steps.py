# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]

sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500,
                "GOES"     : 2000,
                "worldview": 0.31
               }

print("I have the following satellites in my database:", sat_database.keys())

# 2) print out all satellite names contained in the dictionary [2P]
print(sat_database.keys())
# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]
search = input("Which sattelite are you searching ? ")
# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]
answer = search in sat_database
if answer == True:
    print("Your sattelite exists in this database! ")
elif answer == False:
    print("Your sattelite is not found in this database! ")
# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 
if search == "METEOSAT":
    print("The METEOSAT-sattelite has a resolution of 3000.")
elif search == "LANDSAT":
    print("The LANDSAT-sattelite has a resolution of 30.")
elif search == "MODIS":
    print("The MODIS-sattelite has a resolution of 500.")
elif search == "GOES":
    print("The GOES-sattelite has a resolution of 2000.")
elif search == "worldview":
    print("The worldview-sattelite has a resolution of 0.31.")
else:
    print("Try a new search.")
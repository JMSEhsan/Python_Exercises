print("\n\t\033[1;30;47m Ehsan *** Feb. 10, 2021 *** Team IV *** Assignment Day 8 \033[0;37;40m\n")

#1&5
import re
txt = "(000)000-0000 ext:000"
try:
    x = re.findall("[(]\d{3}[])]\d{3}-\d{4}\sext:\d{3}", txt)
    print("#1- Finding phone # patter: ", x, "\n")
except:
    print("something went wrong")

#2&5
import json
try:
    f = open("C:\\Users\\se_ja\\OneDrive\\Documents\\f\\JSON\\students.json", "r")
    k = json.loads(f.read())
    print("#2- Opening and creating a Python object: ", k, "   type: ", type(k))
    f.close()
except:
    print("something went wrong")

#3&5
try:
    for x, y in k[1].items():
        if x == "Marks":
            tdic = y
            y.update({"Science": 84})
    print("\n#3- Sam's Science mark updated: ", y.get("Science"))
except:
    print("something went wrong")

#4&5
try:
    kJsn = json.dumps(k, indent = 3)
    g = open("C:\\Users\\se_ja\\OneDrive\\Documents\\f\\JSON\\students.json", "w") 
    g.write(kJsn)
    g.close()
    print("\n#4- Overwrite updated student information: ", kJsn)
except:
    print("something went wrong")

#6 
import pyowm

print("\n#6 - Setting up weather API to get weather data: \n") 

APIKEY='21f8fda7773dc1abf6e7afd3b9a36d80'                  
OpenWMap=pyowm.OWM(APIKEY)                   
Weather=OpenWMap.weather_at_place("Calgary")  
Data=Weather.get_weather()                   

temp = Data.get_temperature(unit='celsius')      
print ("Average Temp. Currently ", temp['temp']) 
print ("Max Temp. Currently ", temp['temp_max']) 
print ("Min Temp. Currently ", temp['temp_min']) 

humidity = Data.get_humidity() 
print ("Humidity : ",humidity)  

humidity = Data.get_humidity()  
print ("Humidity : ",humidity)  

cloud = Data.get_clouds() 
print ("Cloud Coverage Percentage : ",cloud) 

Data.get_sunset_time() 
Data.get_sunrise_time() 
Data.get_pressure() 
Data.get_status() 
Data.get_detailed_status() 

Weatherforecast = OpenWMap.three_hours_forecast("Calgary") 
rain=Weatherforecast.will_have_rain()
sun=Weatherforecast.will_have_sun() 
cloud=Weatherforecast.will_have_clouds() 

print("There will be rain :",rain) 
print("There will be sun :",sun) 
print("There will be clouds :",cloud) 

time = '2021-02-12 09:30:00+00'   

rain=Weatherforecast.will_be_rainy_at(time) 
sun=Weatherforecast.will_be_sunny_at(time) 
cloud=Weatherforecast.will_be_cloudy_at(time) 

print("There will be rain :",rain) 
print("There will be sun :",sun) 
print("There will be clouds :",cloud) 

print("\n  *** END ***   \n")
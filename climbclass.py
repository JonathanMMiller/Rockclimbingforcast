import time
from datetime import date, datetime
import requests
import json

#Weather bit API key and URL's for Forcast weather 5day/3hr and One call
API_KEY = "5d9497b5255fd5bcfd39e0068cdbe045"

#For each desired climbing location need to input Name, Latitude and Longitude this will retrieve Weather API data for prev 48hrs,and a 5day/3hr forcast of key weather data
class ClimbLocation():
  def __init__ (self,name,lat,lon):
    self.name = name
    self.lat = lat
    self.lon = lon
    self.accumrain = []
    self.forcast = []
#will request a json file for the lat and lon of the object instance and parse data from request, parse Json file, and add conditional variables return dict to self.forcast attribute
  def requestforcast(self):
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
    request_url = f"{BASE_URL}?lat={self.lat}&lon={self.lon}&appid={API_KEY}&units=imperial"
    forcastdata = requests.get(request_url).json()
       
    #creates empty dictionary to append values which will be stored in .forcast
    #"Dayofweek":[], "Time 12hr":[], 'Dateshort':[],
    atr_dict = {'dt': [],'Inches rain': [],'Temperature F': [],
                'Wind mph': [],'Cloud Cover %':[]}
    
#loops through forcast data filling dictionary lists with json key values 
    for i in forcastdata['list']:
      dt = datetime.fromisoformat(i['dt_txt'])
      atr_dict['dt'].append(dt.strftime('%a %I%p'))
      if 'rain' in i:
        atr_dict['Inches rain'].append(round(i['rain']['3h']*0.0393701,4))
      else:
        atr_dict['Inches rain'].append(0.0)
      atr_dict['Temperature F'].append(i['main']['temp'])
      atr_dict['Cloud Cover %'].append(i['clouds']['all'])
      atr_dict['Wind mph'].append(i['wind']['speed'])
    return(atr_dict)
#loops through rain data and appends raincond condition variable   
  def conditiondata(self,atr_dict):
    cond_dict = {'raincond':[],'tempcond':[],'windcond':[]} 
    for i in atr_dict['Inches rain']:
      if i >= 0.01: 
        cond_dict['raincond'].append(round(1+i*100,3))       
      else: 
        cond_dict['raincond'].append(1.0)
    #loops through Wind data and appends Windcond condition variable 
    for i in atr_dict['Wind mph']:
      if i <= 5: 
        cond_dict['windcond'].append(1.0)
      else:
         cond_dict['windcond'].append(0.1*i+0.5)
        
    #loops through Temp data and appends tempcond condition variable  
    for i in atr_dict['Temperature F']:
      if i >= 90: 
        cond_dict['tempcond'].append(4.0)
      elif 80 <= i < 90:
        cond_dict['tempcond'].append(3.0)
      elif 75 <= i < 80:
        cond_dict['tempcond'].append(2.0)
      elif 65 <= i < 75:
        cond_dict['tempcond'].append(1.0)
      elif 55 <= i < 65:
        cond_dict['tempcond'].append(2.0)
      elif 40 <= i < 55:
        cond_dict['tempcond'].append(3.0)
      else: 
        cond_dict['tempcond'].append(4.0)
   
    #Converts date text to a datetime class attribute seperates into
    #Dayofweek, 12 hr time, and a short date
    
    # for i in atr_dict['dt']:
    #   dt = datetime.fromisoformat(i)
    #   atr_dict['Dayofweek'].append(dt.strftime("%A"))
    #   atr_dict['Time 12hr'].append(dt.strftime("%I %p"))
    #   atr_dict['Dateshort'].append(dt.strftime("%d-%m-%y"))
    #returns a filled and modified dictionary with all key values

    return(cond_dict)
  
#Requests one call WeatherAPI prev 48hrs, totals rain , returns summed rainfall store in.selfaccum)_rain
  def getaccumrain(self):
    BASE_URL = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
    
    #variable for uniex time to make 2 calls for each 24 period by hour
    oneday = int(time.time()-(60 * 60 * 24))
    twoday = int(time.time()-(60 * 60 * 24*2))
    
    #generates urls
    request_url = f"{BASE_URL}?lat={self.lat}&lon={self.lon}&dt={twoday}&appid={API_KEY}"
    request_url2 = f"{BASE_URL}?lat={self.lat}&lon={self.lon}&dt={oneday}&appid={API_KEY}"
    #requests data based on URL +API_Key
    data = requests.get(request_url).json()
    data2 = requests.get(request_url2).json()
    
    #Creates empty list to append hourly data
    hist_rain = []
    #loops through json file and collects rain data if it exists appends to hist_rain list (need to combine for loops )
    for i in data['hourly']:
      if 'rain' in i:
        hist_rain.append(i['rain']['1h'])
      else:
        hist_rain.append(0.0)
    for i in data2['hourly']:
      if 'rain' in i:
        hist_rain.append(i['rain']['1h'])
      else:
        hist_rain.append(0.0)
    accum_rain = round(sum(hist_rain) * 0.0393701,4) 
    return (accum_rain)

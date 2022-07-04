import requests
import datetime as dt
import os
today = dt.datetime.now()
time = dt.datetime.now()
APP_ID = os.environ.get("app_id")
API_KEY = os.environ.get("api_key")
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
ADD_ROW_POINT = os.environ.get("sheet_endpoint")
USER_NAME = os.environ.get("user_name")
PASSWORD =  os.environ.get("password")
AGE=36
weight_kg =85.2
height_cm = 172.72
exercise_performed = input("What exercise did you do?:")
headers = {
 "x-app-id": APP_ID,
 "x-app-key":API_KEY ,
 "Content-Type": "application/json",

}

parameters ={
 "query": exercise_performed,
 "gender":"male",
 "weight_kg":weight_kg,
 "height_cm":height_cm,
 "age":AGE
}
response = requests.post(url= END_POINT, json=parameters, headers=headers)
result = response.json()

for things in result['exercises']:
   add_parameters ={
     "workout": {
        "date": today.strftime("%Y/%d/%m"),
        "time": time.strftime("%X"),
        "exercise": things['user_input'].title(),
        "duration": things['duration_min'],
        "calories": things['nf_calories'],
  }
}
   response = requests.post(url=ADD_ROW_POINT, json=add_parameters, auth=(
      USER_NAME,
      PASSWORD,
  )
)
   data = response.json()
print(response.text)



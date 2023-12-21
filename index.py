#enter input
#show weather of that location from weather api


import requests



input_val = ""
api_host = "weatherapi-com.p.rapidapi.com"
api_key = "c256ecdf6emshcedc5242d337c13p19a862jsnee79af877651"
while input_val != "exit":
    input_val= input("enter location : \n")
    url = f"https://weatherapi-com.p.rapidapi.com/current.json?q={input_val}"
    headers = {
          "X-RapidAPI-Host": api_host,
        "X-RapidAPI-Key": api_key
    }
    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        
        
        respJson = response.json()
        
        location = f"{respJson["location"]["name"]},{respJson["location"]["region"]}"
        temp = f"{respJson["current"]["temp_c"]} celsius"
        condition = respJson["current"]["condition"]["text"]
        print(
            f"temperature is {temp} at {location} and it seems {condition}"
        )
    elif 400:
        print("invalid location")
    else:
        print("server error")
    

